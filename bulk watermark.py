from PIL import Image
import os

# set the path to the main folder containing the subfolders
main_folder_path = "E:\\AMAZON TOP SELLING"

# set the desired width and height
width = 600
height = 600

# Load the logo image
logo = Image.open("E:\\Personal\\myntra amazon codes\\LOGO\\amazon.png")

for i in range(1, 101):
    
    subfolder_path = os.path.join(main_folder_path, str(i))
    
    if os.path.exists(subfolder_path):
        
        for filename in os.listdir(subfolder_path):
           
            if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".bmp"):
                
                img = Image.open(os.path.join(subfolder_path, filename))
                
                current_ratio = img.size[0] / img.size[1]
                
                if current_ratio > 1:
                    new_width = width
                    new_height = int(width / current_ratio)
                else:
                    new_width = int(height * current_ratio)
                    new_height = height
                
                img = img.resize((new_width, new_height), Image.LANCZOS)
                
                new_img = Image.new("RGB", (width, height), color=(255, 255, 255))
                
                x_offset = int((width - new_width) / 2)
                y_offset = int((height - new_height) / 2)
                new_img.paste(img, (x_offset, y_offset))
                
                # Paste the logo in the top-right corner of the image
                logo_size = tuple([int(x/4) for x in logo.size])
                logo_resized = logo.resize(logo_size)
                position = (12, 12)
                new_img.paste(logo_resized, position, logo_resized)
                
                new_folder_path = os.path.join(main_folder_path, "resized")
                os.makedirs(new_folder_path, exist_ok=True)
                new_file_path = os.path.join(new_folder_path, str(i), filename)
                os.makedirs(os.path.dirname(new_file_path), exist_ok=True)
                new_img.save(new_file_path)
