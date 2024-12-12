import os

root_folder_path = "PATH"  # replace with your root folder path
prefix = "$BL"  # replace with your desired prefix
suffix = "000"  # replace with your desired suffix

for dirpath, dirnames, filenames in os.walk(root_folder_path):
    if "BLANK" in dirnames:
        blank_folder_path = os.path.join(dirpath, "BLANK")
        for filename in os.listdir(blank_folder_path):
            if os.path.isfile(os.path.join(blank_folder_path, filename)):
                # split filename and extension
                basename, extension = os.path.splitext(filename)
                # add prefix and suffix to filename
                new_filename = prefix + basename + suffix + extension
                # rename file with new filename
                os.rename(os.path.join(blank_folder_path, filename), os.path.join(blank_folder_path, new_filename))
