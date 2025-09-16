import base64
import os

# List of artifact example images to convert
image_files = ['Snooz_logo.png']

# Variable names for each image
variable_names = ['SNOOZ_LOGO_IMAGE_BASE64']

# Get script directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Create the data file
output_file = os.path.join(script_dir, 'art_image_data.py')

with open(output_file, 'w') as f:
    f.write('"""\n')
    f.write('Base64 encoded artifact example images\n')
    f.write('"""\n\n')
    
    for image_file, var_name in zip(image_files, variable_names):
        try:
            with open(os.path.join(script_dir, image_file), 'rb') as img_f:
                image_data = base64.b64encode(img_f.read()).decode()
                f.write(f'{var_name} = """\n')
                f.write(image_data)
                f.write('\n""".strip()\n\n')
        except FileNotFoundError:
            print(f"Warning: {image_file} not found in {script_dir}")
            f.write(f'{var_name} = ""\n\n')

print(f"Created {output_file}")
