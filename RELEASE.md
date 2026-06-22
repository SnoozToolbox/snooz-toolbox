# Snooz Release Strategy

Snooz follows a release-candidate workflow to ensure that installers and packages are validated on all supported operating systems before an official release is published.

## Release Branch

When preparing a new release, create a dedicated release branch from `main`:

```text
main
 └─ release/X.Y.Z
```

For example:

```text
release/1.0.0
```

Only bug fixes and release-related changes should be committed to the release branch. New features must continue to be developed on `main`.

## Release Candidates

All validation builds are published as release candidates (RCs). The application version, installer version, Git tag, and GitHub release must use the same version number.

Examples:

```text
1.0.0-rc.1
1.0.0-rc.2
1.0.0-rc.3
```

For each release candidate:

1. Update the Snooz version number.
2. Build installers for all supported platforms.
3. Create a Git tag matching the version.
4. Publish a GitHub pre-release.

Example:

```text
Version: 1.0.0-rc.1
Tag:     v1.0.0-rc.1
Release: GitHub Pre-release
```

If issues are found during validation, fix them on the release branch, increment the RC number, and publish a new release candidate.

## Tagging Policy

Git tags must be immutable and should never be moved or reused.

Each release candidate receives its own unique tag:

```text
v1.0.0-rc.1
v1.0.0-rc.2
v1.0.0-rc.3
```

This ensures that bug reports, installers, and build artifacts can always be traced back to the exact source code used to generate them.

## Final Release

Once all release candidates have been validated successfully:

1. Update the version number to the final release version.

```text
1.0.0
```

2. Commit the version change.
3. Create the final tag:

```text
v1.0.0
```

4. Publish the official GitHub release (not marked as a pre-release).
5. Merge the release branch back into `main`.

Example:

```text
main
 ├─ release/1.0.0
 └─ v1.0.0
```

## Benefits

This workflow provides:

* Stable and reproducible releases.
* Clear traceability between source code and installers.
* Safe validation of installers on Windows, macOS, and Linux.
* Reduced risk of users installing unfinished builds.
* Consistent versioning across Snooz, packages, installers, and GitHub releases.

```
```
