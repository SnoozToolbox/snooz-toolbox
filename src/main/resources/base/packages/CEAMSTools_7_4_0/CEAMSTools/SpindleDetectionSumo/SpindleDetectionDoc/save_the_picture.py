import base64
import os

# Get the directory where this script is located (or specify the target directory)
script_dir = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(script_dir, 'spindle_image_data.py')

# Read and encode the PNG file
with open(script_dir + '/'+'e0004-b1-01-05-0001-smp303751_res80.png', 'rb') as f:
    image_data = base64.b64encode(f.read()).decode()

# Write to the spindle_image_data.py file
with open(output_file, 'w') as f:
    f.write('"""\n')
    f.write('Base64 encoded spindle image data\n')
    f.write('"""\n\n')
    f.write('SPINDLE_IMAGE_BASE64 = """\n')
    f.write(image_data)
    f.write('\n""".strip()\n')

print(f"Successfully created {output_file}")