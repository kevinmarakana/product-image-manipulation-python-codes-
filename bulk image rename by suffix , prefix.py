import os
from PIL import Image

user_name = "WH"
root_folder = "D:\\update\\30 WOMEN'S HEALS"

for root, dirs, files in os.walk(root_folder):
    counter = 1  # reset the counter for each subfolder
    for filename in files:
        filepath = os.path.join(root, filename)
        try:
            img = Image.open(filepath)
            img.verify()  # check if the file is a valid image
            folder_name = os.path.basename(root)
            
            file_extension = os.path.splitext(filename)[1]
            new_filename = f"{user_name}_{folder_name}_{counter}{file_extension}"
            new_filepath = os.path.join(root, new_filename)
            os.rename(filepath, new_filepath)
            print(f"Renamed {filename} to {new_filename}")
            counter += 1  # increment the counter for the next file
        except (IOError, SyntaxError):
            print(f"Skipping {filename}, not an image file.")
