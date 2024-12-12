from PIL import Image
import os

# Set the root directory path
root_dir = "D:\\work\\"
# Loop through each subdirectory in the root directory
for sub_dir in os.listdir(root_dir):
    sub_dir_path = os.path.join(root_dir, sub_dir)
    if os.path.isdir(sub_dir_path):
        # Loop through each file in the COLOR1 folder in the subdirectory
        color1_dir_path = os.path.join(sub_dir_path, "output")
        color_dir_path = os.path.join(sub_dir_path, "jpg")
        if os.path.isdir(color1_dir_path) and os.path.isdir(color_dir_path):
            for filename in os.listdir(color1_dir_path):
                if filename.endswith('.psd'):
                    try:
                        # Open the PSD file
                        psd_image = Image.open(os.path.join(color1_dir_path, filename))

                        # Convert the PSD image to JPG
                        jpg_filename = os.path.splitext(filename)[0]
                        output_path = os.path.join(color_dir_path, jpg_filename)
                        psd_image.save(output_path, 'JPEG')
                    except Exception as e:
                        print(f"Error occurred in subdirectory {sub_dir}: {e}. Skipping subdirectory.")
                        break
