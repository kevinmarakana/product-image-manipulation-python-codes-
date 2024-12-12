from PIL import Image
import os

# Set the folder path containing the PSD files
folder_path = "C:\\Users\\KEVIN\\Desktop\\looking cart\\Printed"
# Set the folder path to save the JPG files
output_folder_path = "C:\\Users\\KEVIN\\Desktop\\looking cart\\jpg printed"

# Loop through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.psd'):
        # Open the PSD file
        psd_image = Image.open(os.path.join(folder_path, filename))

        # Convert the PSD image to JPG
        jpg_filename = os.path.splitext(filename)[0]
        output_path = os.path.join(output_folder_path, jpg_filename)
        psd_image.save(output_path, 'JPEG')
