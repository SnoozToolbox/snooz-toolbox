import base64
import os

# List of image files to convert
image_files = [
    'UI_v5_minimal.png',
    'UI_v5_Aeschbach.png', 
    'UI_v5_Feinberg_floyd.png'
]

# Variable names for each image
variable_names = [
    'MINIMAL_IMAGE_BASE64',
    'AESCHBACH_IMAGE_BASE64',
    'FEINBERG_FLOYD_IMAGE_BASE64'
]

# Get the directory where this script is located (or specify the target directory)
script_dir = os.path.dirname(os.path.abspath(__file__))

# Create the data file
output_file = os.path.join(script_dir, 'sleep_cycle_image_data.py')

with open(output_file, 'w') as f:
    f.write('"""\n')
    f.write('Base64 encoded sleep cycle delimiter images\n')
    f.write('"""\n\n')
    
    for image_file, var_name in zip(image_files, variable_names):
        try:
            with open(os.path.join(script_dir,image_file), 'rb') as img_f:
                image_data = base64.b64encode(img_f.read()).decode()
                f.write(f'{var_name} = """\n')
                f.write(image_data)
                f.write('\n""".strip()\n\n')
                print(f"Converted {image_file} -> {var_name}")
        except FileNotFoundError:
            print(f"Warning: {image_file} not found, skipping...")

print(f"Successfully created {output_file}")