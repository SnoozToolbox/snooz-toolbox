import base64
import os

# List of artifact example images to convert
image_files = [
    '2_amplitude_v2.png',
    '3_burst_noise_v2.png',
    '3b_persistent_noise.png',
    '4_powerLine_v2.png',
    '5_BSLVar_v2.png',
    '6_muscular_v2.png'
]

# Variable names for each image
variable_names = [
    'AMPLITUDE_IMAGE_BASE64',
    'BURST_NOISE_IMAGE_BASE64',
    'PERSISTENT_NOISE_IMAGE_BASE64',
    'POWER_LINE_IMAGE_BASE64',
    'BSL_VAR_IMAGE_BASE64',
    'MUSCULAR_IMAGE_BASE64'
]

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
                print(f"Converted {image_file} -> {var_name}")
        except FileNotFoundError:
            print(f"Warning: {image_file} not found, skipping...")

print(f"Successfully created {output_file}")