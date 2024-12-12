from PIL import Image
import os

# Set the path to the main folder containing the subfolders
main_folder_path = "C:\\Users\\KEVIN\\Desktop\\looking cart\\watches\\Watch Images"

# Set the desired width and height
width = 1080
height = 1210

# Get all subfolders within the main folder
subfolders = [folder for folder in os.listdir(main_folder_path) if os.path.isdir(os.path.join(main_folder_path, folder))]

# Loop through each subfolder
for subfolder_name in subfolders:
    # Set the path to the current subfolder
    subfolder_path = os.path.join(main_folder_path, subfolder_name)
    # Loop through each file in the subfolder
    for filename in os.listdir(subfolder_path):
        # Check if the file is a supported image file (e.g. .jpg, .png, .bmp)
        if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".bmp"):
            # Open the image using Pillow
            img = Image.open(os.path.join(subfolder_path, filename))
            # Get the current aspect ratio
            current_ratio = img.size[0] / img.size[1]
            # Calculate the new dimensions while maintaining the aspect ratio
            if current_ratio > 1:
                new_width = width
                new_height = int(width / current_ratio)
            else:
                new_width = int(height * current_ratio)
                new_height = height
            # Resize the image using Lanczos interpolation for best quality
            img = img.resize((new_width, new_height), Image.LANCZOS)
            # Create a new blank image with the desired dimensions
            new_img = Image.new("RGB", (width, height), color="#e2e1e6")
            # Paste the resized image in the center of the new image
            x_offset = int((width - new_width) / 2)
            y_offset = int((height - new_height) / 2)
            new_img.paste(img, (x_offset, y_offset))
            # Save the image with the same filename but in a new folder
            new_folder_path = os.path.join(main_folder_path, "resized")
            os.makedirs(new_folder_path, exist_ok=True)
            new_file_path = os.path.join(new_folder_path, subfolder_name, filename)
            os.makedirs(os.path.dirname(new_file_path), exist_ok=True)
            new_img.save(new_file_path)
