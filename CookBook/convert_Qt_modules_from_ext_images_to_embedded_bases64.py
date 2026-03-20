#!/usr/bin/env python3
"""
Script to convert Qt modules from external image files to embedded base64 images.
Automatically applies all necessary modifications to .ui and .py files.
"""

import os
import re
import base64
import shutil
from pathlib import Path

def find_png_files(folder_path):
    """Find all PNG files in the folder."""
    png_files = []
    for file in os.listdir(folder_path):
        if file.endswith('.png') or file.endswith('.jpg'):
            png_files.append(file)
    return png_files

def create_variable_names(png_files):
    """Convert image filenames to BASE64 variable names."""
    variable_names = []
    for image_file in png_files:
        # Remove extension and convert to uppercase
        base_name = os.path.splitext(image_file)[0]
        # Convert to uppercase
        name = base_name.upper()
        # Replace special characters with underscores
        name = re.sub(r'[^A-Z0-9]', '_', name)
        name += '_IMAGE_BASE64'
        variable_names.append(name)
    return variable_names

def create_conversion_script(folder_path, png_files, variable_names):
    """Create the create_images_file.py script."""
    script_content = f'''import base64
import os

# List of artifact example images to convert
image_files = {png_files}

# Variable names for each image
variable_names = {variable_names}

# Get script directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Create the data file
output_file = os.path.join(script_dir, 'art_image_data.py')

with open(output_file, 'w') as f:
    f.write('"""\\n')
    f.write('Base64 encoded artifact example images\\n')
    f.write('"""\\n\\n')
    
    for image_file, var_name in zip(image_files, variable_names):
        try:
            with open(os.path.join(script_dir, image_file), 'rb') as img_f:
                image_data = base64.b64encode(img_f.read()).decode()
                f.write(f'{{var_name}} = """\\n')
                f.write(image_data)
                f.write('\\n""".strip()\\n\\n')
        except FileNotFoundError:
            print(f"Warning: {{image_file}} not found in {{script_dir}}")
            f.write(f'{{var_name}} = ""\\n\\n')

print(f"Created {{output_file}}")
'''
    
    script_path = os.path.join(folder_path, 'create_images_file.py')
    with open(script_path, 'w') as f:
        f.write(script_content)
    
    return script_path

def find_labels_with_pixmaps_and_images(ui_file_path):
    """Find QLabel widgets with pixmap properties and extract their image filenames."""
    label_image_pairs = []
    
    with open(ui_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all QLabel widgets first
    label_widgets = re.findall(r'<widget class="QLabel" name="([^"]+)"[^>]*>(.*?)</widget>', content, re.DOTALL)
    
    # Check which ones have pixmap properties and extract image filename
    for label_name, widget_content in label_widgets:
        # Updated regex to match both .png and .jpg files
        pixmap_match = re.search(r'<property name="pixmap">.*?([^<>/]+\.(png|jpg))', widget_content, re.DOTALL)
        if pixmap_match:
            image_filename = pixmap_match.group(1)
            label_image_pairs.append((label_name, image_filename))
    
    return label_image_pairs

def remove_pixmap_properties(ui_file_path, labels):
    """Remove pixmap properties from QLabel widgets in UI file."""
    with open(ui_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove pixmap properties for each label
    for label in labels:
        pattern = f'(<widget class="QLabel" name="{label}"[^>]*>.*?)<property name="pixmap">.*?</property>(.*?</widget>)'
        replacement = r'\1<property name="text"><string/></property>\2'
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    # Remove resource includes (keep only themes.qrc)
    content = re.sub(r'<include location="[^"]*(?<!themes)\.qrc"/>\s*\n', '', content)
    
    with open(ui_file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def update_python_file(py_file_path, labels, variable_names):
    """Update Python file to load embedded images."""
    with open(py_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find where to insert imports (after header but before other imports)
    lines = content.split('\n')
    insert_index = 0
    
    # Skip shebang, docstrings, and comments at the beginning
    for i, line in enumerate(lines):
        stripped = line.strip()
        # Skip shebang
        if stripped.startswith('#!'):
            continue
        # Skip docstrings (triple quotes)
        if stripped.startswith('"""') or stripped.startswith("'''"):
            # Find end of docstring
            quote_type = '"""' if stripped.startswith('"""') else "'''"
            if stripped.count(quote_type) == 2:  # Single line docstring
                insert_index = i + 1
                continue
            else:  # Multi-line docstring
                for j in range(i + 1, len(lines)):
                    if quote_type in lines[j]:
                        insert_index = j + 1
                        break
                break
        # Skip comments
        if stripped.startswith('#'):
            continue
        # Found first non-header line
        if stripped and not stripped.startswith(('"""', "'''", '#')):
            insert_index = i
            break
    
    # Add imports at the correct position
    imports_to_add = []
    
    if 'import base64' not in content:
        imports_to_add.append('import base64')
    
    if 'QPixmap' not in content:
        if 'from qtpy.QtGui import' in content:
            # Add QPixmap to existing QtGui import
            for i, line in enumerate(lines):
                if 'from qtpy.QtGui import' in line and 'QPixmap' not in line:
                    if line.strip().endswith('import'):
                        lines[i] = line + ' QPixmap'
                    else:
                        lines[i] = line.replace('import', 'import QPixmap,')
                    break
        else:
            imports_to_add.append('from qtpy.QtGui import QPixmap')
    
    # Insert new imports
    for imp in reversed(imports_to_add):
        lines.insert(insert_index, imp)
    
    content = '\n'.join(lines)
    
    # Create image loading method
    if len(labels) == 1:
        # Single image
        method_content = f'''
    def _load_embedded_image(self):
        """Load the embedded base64 image data into {labels[0]}."""
        from .art_image_data import {variable_names[0]}
        
        image_bytes = base64.b64decode({variable_names[0]})
        pixmap = QPixmap()
        pixmap.loadFromData(image_bytes)
        self.{labels[0]}.setPixmap(pixmap)
'''
        method_call = '        self._load_embedded_image()'
    else:
        # Multiple images
        imports = ', '.join(variable_names)
        mappings = ', '.join([f'self.{label}: {var}' for label, var in zip(labels, variable_names)])
        
        method_content = f'''
    def _load_embedded_images(self):
        """Load the embedded base64 image data into the QLabel widgets."""
        from .art_image_data import {imports}
        
        image_mappings = {{{mappings}}}
        
        for label, base64_data in image_mappings.items():
            image_bytes = base64.b64decode(base64_data)
            pixmap = QPixmap()
            pixmap.loadFromData(image_bytes)
            label.setPixmap(pixmap)
'''
        method_call = '        self._load_embedded_images()'
    
    # Insert method call after setupUi
    init_pattern = r'(def __init__\(self, \*\*kwargs\):.*?self\.setupUi\(self\))'
    replacement = f'\\1\n{method_call}'
    content = re.sub(init_pattern, replacement, content, flags=re.DOTALL)
    
    # Add method before load_settings
    load_settings_pattern = r'(\n    def load_settings\(self\):)'
    content = re.sub(load_settings_pattern, f'{method_content}\\1', content)
    
    with open(py_file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def convert_folder(folder_path):
    """Convert a single folder to use embedded base64 images."""
    print(f"Converting folder: {folder_path}")
    
    # Find PNG files
    png_files = find_png_files(folder_path)
    if not png_files:
        print(f"  No PNG files found in {folder_path}")
        return
    
    # Find UI file and extract label-image mappings
    ui_files = [f for f in os.listdir(folder_path) if f.endswith('.ui')]
    if not ui_files:
        print(f"  No UI file found in {folder_path}")
        return
    
    ui_file_path = os.path.join(folder_path, ui_files[0])
    label_image_pairs = find_labels_with_pixmaps_and_images(ui_file_path)
    
    if not label_image_pairs:
        print(f"  No labels with pixmaps found in {ui_files[0]}")
        return
    
    # Create matched variable names
    labels = []
    variable_names = []
    matched_png_files = []
    
    for label_name, image_filename in label_image_pairs:
        if image_filename in png_files:
            labels.append(label_name)
            var_name = image_filename.replace('.png', '').upper()
            var_name = re.sub(r'[^A-Z0-9]', '_', var_name) + '_IMAGE_BASE64'
            variable_names.append(var_name)
            matched_png_files.append(image_filename)
    
    print(f"  Matched labels to images: {list(zip(labels, matched_png_files))}")
    
    # Create conversion script with matched files
    script_path = create_conversion_script(folder_path, matched_png_files, variable_names)
    print(f"  Created: {script_path}")
    
    # Run conversion script
    os.system(f'cd "{folder_path}" && python create_images_file.py')
    
    # Remove pixmap properties from UI
    remove_pixmap_properties(ui_file_path, labels)
    print(f"  Updated UI file: {ui_files[0]}")
    
    # Update Python file with correct label-variable mapping
    py_files = [f for f in os.listdir(folder_path) if f.endswith('.py') and not f.startswith('Ui_') and f != 'create_images_file.py' and f != 'art_image_data.py']
    if py_files:
        py_file_path = os.path.join(folder_path, py_files[0])
        update_python_file(py_file_path, labels, variable_names)
        print(f"  Updated Python file: {py_files[0]}")
    
    print(f"  ✅ Conversion completed for {folder_path}")

def main():
    """Main function to process folders."""
    # Edit this path to point to your target folder or parent folder
    BASE_PATH = r"C:\Users\klacourse\Documents\snooz_workspace\snooz-package-ceams\modules\CEAMSModules"
    

    # If BASE_PATH is a single folder, convert it
    # If BASE_PATH contains subfolders, convert all subfolders
    
    if not os.path.exists(BASE_PATH):
        print(f"Error: Path does not exist: {BASE_PATH}")
        return
    
    if os.path.isfile(BASE_PATH):
        print(f"Error: Path is a file, not a directory: {BASE_PATH}")
        return
    
    # Check if BASE_PATH contains Python files (single module) or subfolders
    py_files = [f for f in os.listdir(BASE_PATH) if f.endswith('.py')]
    
    if py_files:
        # Single module folder
        convert_folder(BASE_PATH)
    else:
        # Parent folder with subfolders
        subfolders = [f for f in os.listdir(BASE_PATH) if os.path.isdir(os.path.join(BASE_PATH, f))]
        
        for subfolder in subfolders:
            subfolder_path = os.path.join(BASE_PATH, subfolder)
            try:
                convert_folder(subfolder_path)
            except Exception as e:
                print(f"  ❌ Error converting {subfolder_path}: {e}")
    
    print("🎉 All conversions completed!")

if __name__ == "__main__":
    main()