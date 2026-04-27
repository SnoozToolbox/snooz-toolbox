"""
Sync per-item JSON files with their package manifest (CEAMSTools, CEAMSModules, CEAMSApps).

Updates only version-related string values in-place (no full re-serialization), preserving
key order, whitespace, and newlines in each file.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Dict, List, Tuple


def _toolbox_project_root() -> Path:
    """src/main/python/... -> repository root (same rule as runtime ApplicationContext)."""
    here = Path(__file__).resolve().parent
    result = here
    while result != result.parent:
        if (result / "src" / "main" / "python").is_dir():
            return result
        result = result.parent
    raise RuntimeError(
        "Could not locate snooz-toolbox project root (expected src/main/python)."
    )


def _embedded_packages_root() -> Path:
    return _toolbox_project_root() / "src" / "main" / "resources" / "base" / "packages"


def _read_text_preserve_newlines(path: Path) -> str:
    with path.open("r", encoding="utf-8", newline="") as f:
        return f.read()


def _write_text_preserve_newlines(path: Path, text: str) -> None:
    with path.open("w", encoding="utf-8", newline="") as f:
        f.write(text)


def _load_json(path: Path) -> Dict[str, Any]:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def _find_manifests_under(root: Path, package_folder: str, manifest_name: str) -> List[Path]:
    if not root.is_dir():
        return []
    out: List[Path] = []
    for child in root.iterdir():
        if not child.is_dir():
            continue
        candidate = child / package_folder / manifest_name
        if candidate.is_file():
            out.append(candidate)
    return sorted(out)


def _bundle_suffix_from_version_folder(version_folder: Path) -> str | None:
    """
    e.g. CEAMSTools_7_3_0 -> 7_3_0, CEAMSModules_7_4_0 -> 7_4_0.
    Used so multiple versioned folders under packages/ do not overwrite each other.
    """
    name = version_folder.name
    for prefix in ("CEAMSTools_", "CEAMSModules_", "CEAMSApps_"):
        if name.startswith(prefix):
            return name[len(prefix) :]
    return None


def _collect_package_versions_for_bundled_suffix(
    packages_root: Path, suffix: str
) -> Dict[str, str]:
    """
    Read CEAMSTools_{suffix}, CEAMSModules_{suffix}, CEAMSApps_{suffix} manifests only.

    If a sibling folder for this suffix is missing, that package_name is omitted
    (dependency lines for that package are left unchanged).
    """
    versions: Dict[str, str] = {}
    triples = (
        ("CEAMSTools", "CEAMSTools", "CEAMSTools.json"),
        ("CEAMSModules", "CEAMSModules", "CEAMSModules.json"),
        ("CEAMSApps", "CEAMSApps", "CEAMSApps.json"),
    )
    for top_prefix, inner, manifest_name in triples:
        path = packages_root / f"{top_prefix}_{suffix}" / inner / manifest_name
        if path.is_file():
            _merge_manifest_version(versions, path)
    return versions


def _collect_package_versions_from_bundled_layout(packages_root: Path) -> Dict[str, str]:
    """Fallback: merge every CEAMS* manifest under packages/ (last path wins per package_name)."""
    versions: Dict[str, str] = {}
    for folder, manifest in (
        ("CEAMSTools", "CEAMSTools.json"),
        ("CEAMSModules", "CEAMSModules.json"),
        ("CEAMSApps", "CEAMSApps.json"),
    ):
        for path in _find_manifests_under(packages_root, folder, manifest):
            _merge_manifest_version(versions, path)
    return versions


def _merge_manifest_version(versions: Dict[str, str], manifest_path: Path) -> None:
    try:
        data = _load_json(manifest_path)
    except (OSError, json.JSONDecodeError):
        return
    pkg = data.get("package_name")
    ver = data.get("package_version")
    if isinstance(pkg, str) and isinstance(ver, str):
        versions[pkg] = ver


def _resolve_package_versions(manifest_path: Path) -> Dict[str, str]:
    """
    Build package_name -> package_version for dependency rewrites.

    Supports (1) toolbox resources: .../packages/NAME_x_y/NAME/*.json
    and (2) snooz-package-ceams-style repo: repo/tools/..., repo/modules/...
    """
    manifest_path = manifest_path.resolve()
    package_dir = manifest_path.parent
    version_folder = package_dir.parent
    versions: Dict[str, str] = {}

    _merge_manifest_version(versions, manifest_path)

    vf = version_folder.name
    if vf.startswith("CEAMSTools_") or vf.startswith("CEAMSModules_") or vf.startswith("CEAMSApps_"):
        packages_root = version_folder.parent
        suffix = _bundle_suffix_from_version_folder(version_folder)
        if suffix is not None:
            versions.update(
                _collect_package_versions_for_bundled_suffix(packages_root, suffix)
            )
        else:
            versions.update(_collect_package_versions_from_bundled_layout(packages_root))
        return versions

    repo_root = version_folder.parent
    peers = [
        repo_root / "tools" / "CEAMSTools" / "CEAMSTools.json",
        repo_root / "modules" / "CEAMSModules" / "CEAMSModules.json",
        repo_root / "apps" / "CEAMSApps" / "CEAMSApps.json",
    ]
    for peer in peers:
        if peer.is_file():
            _merge_manifest_version(versions, peer)
    return versions


def _replace_json_key_string_value(
    text: str, key: str, old: str, new: str, count: int = 0
) -> Tuple[str, bool]:
    """
    Replace JSON '"key": "old"' with '"key": "new"'. `count` is re.subn count (0 = all).
    """
    if old == new:
        return text, False
    pat = re.compile(f'("{re.escape(key)}"\\s*:\\s*)"{re.escape(old)}"')
    new_text, n = pat.subn(lambda m: f'{m.group(1)}"{new}"', text, count=count)
    return new_text, n > 0


def _insert_tool_version_after_tool_params_open(
    text: str, item_version: str
) -> Tuple[str, bool]:
    """Insert a tool_version key when it is missing (immediately after tool_params object '{')."""
    m = re.search(r'"tool_params"\s*:\s*\{', text)
    if not m:
        return text, False
    pos = m.end()
    insert = f'\n        "tool_version": "{item_version}",'
    return text[:pos] + insert + text[pos:], True


def _replace_dep_package_version_anchored(
    text: str, package_name: str, old_ver: str, new_ver: str
) -> Tuple[str, bool]:
    if old_ver == new_ver:
        return text, False
    anchor = f'"package_name": "{package_name}"'
    pos = 0
    while True:
        a = text.find(anchor, pos)
        if a == -1:
            return text, False
        head = a + len(anchor)
        tail = text[head : head + 2000]
        m = re.search(r'"package_version"\s*:\s*"([^"]*)"', tail)
        if m and m.group(1) == old_ver:
            abs_start = head + m.start()
            abs_end = head + m.end()
            new_text = text[:abs_start] + f'"package_version": "{new_ver}"' + text[abs_end:]
            return new_text, True
        pos = a + 1


def _apply_dependency_sync(
    text: str, data: Dict[str, Any], package_versions: Dict[str, str]
) -> Tuple[str, bool]:
    deps = data.get("dependencies")
    if not isinstance(deps, list):
        return text, False
    out = text
    changed = False
    for entry in deps:
        if not isinstance(entry, dict):
            continue
        pname = entry.get("package_name")
        cur = entry.get("package_version")
        if not isinstance(pname, str) or not isinstance(cur, str):
            continue
        if pname not in package_versions or cur == package_versions[pname]:
            continue
        new_v = package_versions[pname]
        out, c = _replace_dep_package_version_anchored(out, pname, cur, new_v)
        changed = changed or c
    return out, changed


def _sync_item_file_text(
    text: str,
    data: Dict[str, Any],
    item_type: str,
    item_version: str,
    package_api_version: str,
    package_versions: Dict[str, str],
) -> Tuple[str, bool]:
    t = text

    cur_api = data.get("item_api_version")
    if isinstance(cur_api, str) and cur_api != package_api_version:
        t, _ = _replace_json_key_string_value(
            t, "item_api_version", cur_api, package_api_version, count=0
        )

    if item_type == "tool":
        tp = data.get("tool_params")
        if isinstance(tp, dict):
            tv = tp.get("tool_version")
            if isinstance(tv, str) and tv != item_version:
                t, _ = _replace_json_key_string_value(
                    t, "tool_version", tv, item_version, count=0
                )
            elif "tool_version" not in tp:
                t, _ = _insert_tool_version_after_tool_params_open(t, item_version)

    t, _ = _apply_dependency_sync(t, data, package_versions)
    return t, t != text


def _parse_item_data(item_path: Path) -> Tuple[str, Dict[str, Any] | None]:
    try:
        text = _read_text_preserve_newlines(item_path)
    except OSError:
        return "", None
    try:
        return text, json.loads(text)
    except json.JSONDecodeError:
        return text, None


def _write_if_changed(path: Path, text: str, new_text: str) -> bool:
    if new_text == text:
        return False
    _write_text_preserve_newlines(path, new_text)
    return True


def _sync_item_file(
    item_path: Path,
    item_type: str,
    item_version: str,
    package_api_version: str,
    package_versions: Dict[str, str],
) -> bool:
    text, data = _parse_item_data(item_path)
    if data is None or not isinstance(data, dict):
        return False

    new_text, any_change = _sync_item_file_text(
        text, data, item_type, item_version, package_api_version, package_versions
    )
    if not any_change:
        return False
    return _write_if_changed(item_path, text, new_text)


def _sync_app_item_file(
    item_path: Path, api_ver: str, package_versions: Dict[str, str]
) -> bool:
    text, data = _parse_item_data(item_path)
    if data is None or not isinstance(data, dict):
        return False

    t = text
    cur_api = data.get("item_api_version")
    if isinstance(cur_api, str) and cur_api != api_ver:
        t, _ = _replace_json_key_string_value(t, "item_api_version", cur_api, api_ver, count=0)

    t, _ = _apply_dependency_sync(t, data, package_versions)
    if t == text:
        return False
    return _write_if_changed(item_path, text, t)


def _sync_manifest_tree(manifest_path: Path) -> int:
    """Return number of item JSON files updated."""
    package_versions = _resolve_package_versions(manifest_path)

    try:
        raw_manifest = _read_text_preserve_newlines(manifest_path)
        manifest = json.loads(raw_manifest)
    except (OSError, json.JSONDecodeError):
        return 0

    api_ver = manifest.get("package_api_version")
    items = manifest.get("items")
    if not isinstance(api_ver, str) or not isinstance(items, list):
        return 0

    package_dir = manifest_path.parent
    updated = 0

    for entry in items:
        if not isinstance(entry, dict):
            continue
        iname = entry.get("item_name")
        itype = entry.get("item_type")
        iver = entry.get("item_version")
        if not isinstance(iname, str) or not isinstance(itype, str) or not isinstance(iver, str):
            continue

        item_json = package_dir / iname / f"{iname}.json"
        if not item_json.is_file():
            continue

        if itype == "app":
            if _sync_app_item_file(item_json, api_ver, package_versions):
                updated += 1
            continue

        if itype in ("tool", "module"):
            if _sync_item_file(item_json, itype, iver, api_ver, package_versions):
                updated += 1

    return updated


# Same parent directory as the snooz-toolbox clone (e.g. …/snooz_workspace/…).
SIBLING_PACKAGE_REPO_DIR_NAME = "snooz-package-ceams"
_PACKAGE_REPO_SUB_MANIFESTS = (
    ("tools/CEAMSTools", "CEAMSTools.json"),
    ("modules/CEAMSModules", "CEAMSModules.json"),
    ("apps/CEAMSApps", "CEAMSApps.json"),
)


def is_valid_snooz_package_repo_root(path: Path) -> bool:
    """True if the tree looks like snooz-package-ceams (has CEAMSTools manifest)."""
    p = path.resolve()
    if not p.is_dir():
        return False
    m = p / "tools" / "CEAMSTools" / "CEAMSTools.json"
    return m.is_file()


def discover_sibling_snooz_package_repo() -> Path | None:
    """
    If snooz-package-ceams sits next to snooz-toolbox, return that path; else None.
    """
    sib = _toolbox_project_root().parent / SIBLING_PACKAGE_REPO_DIR_NAME
    if is_valid_snooz_package_repo_root(sib):
        return sib.resolve()
    return None


def _sync_from_package_repo_root(base: Path) -> int:
    """Run manifest sync for a flat snooz-package-ceams-style repository root."""
    if not base.is_dir():
        return 0
    total = 0
    for rel_folder, manifest in _PACKAGE_REPO_SUB_MANIFESTS:
        mp = base / rel_folder / manifest
        if mp.is_file():
            total += _sync_manifest_tree(mp)
    return total


def sync_embedded_ceams_packages() -> int:
    """
    Scan embedded native packages and align per-item JSON with each manifest.
    """
    root = _embedded_packages_root()
    total = 0
    for folder, manifest in (
        ("CEAMSTools", "CEAMSTools.json"),
        ("CEAMSModules", "CEAMSModules.json"),
        ("CEAMSApps", "CEAMSApps.json"),
    ):
        for manifest_path in _find_manifests_under(root, folder, manifest):
            total += _sync_manifest_tree(manifest_path)
    return total


def run_dev_package_item_version_sync() -> int:
    """
    Dev-only: sync embedded resources and, when present, sibling snooz-package-ceams
    (same parent folder as snooz-toolbox).
    """
    total = sync_embedded_ceams_packages()
    sib = discover_sibling_snooz_package_repo()
    if sib is not None:
        total += _sync_from_package_repo_root(sib)
    return total
