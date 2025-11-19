import os
import shutil  # provide file operations
import re
from datetime import datetime


# Folder where your test files are
source_folder = r"test_data"

# Destination folder where organized files will be stored
destination_folder = r"organized_data"
# File categories (you can expand this dictionary as needed)
file_types = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Data": [".csv", ".xlsx"],
    "Downloads": [".download"],
    "Others": []}
def  create_folder():
    os.makedirs(destination_folder, exist_ok=True)
    for folder in file_types:
        os.makedirs(os.path.join(destination_folder,folder),exist_ok=True)

def rename_file():
    """
      Rename files in the source folder sequentially.
      Example: file_1.txt, file_2.pdf, file_3.jpg ...
      Avoid overwriting existing files by appending a suffix if needed.
      """
    counter = 1
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1].lower()
            new_name = f"file_{counter}{ext}"
            new_path = os.path.join(source_folder, new_name)

            # Avoid overwriting if there is filename exists
            suffix = 1
            while os.path.exists(new_path):
                new_name = f"file_{counter}_{suffix}{ext}"
                new_path = os.path.join(source_folder, new_name)
                suffix += 1

            # Rename the file
            os.rename(file_path, new_path)
            print(f"Renamed: {filename} → {new_name}")

            counter += 1
def move_files():
    """
      Move files from the source folder into the right category subfolders
      inside the destination folder.
      """
    for filename in os.listdir(source_folder):
        old_path = os.path.join(source_folder, filename)

        if os.path.isfile(old_path):
            ext = os.path.splitext(filename)[1].lower()
            moved = False

            # Check each category
            for category, extensions in file_types.items():
                if ext in extensions:
                    # Move file into the matching category
                    new_path = os.path.join(destination_folder, category, filename)
                    shutil.move(old_path, new_path)
                    print(f"Moved: {filename} → {category}")
                    moved = True
                    break

            # If no category matched, put into "Others"
            if not moved:
                new_path = os.path.join(destination_folder, "Others", filename)
                shutil.move(old_path, new_path)
                print(f"Moved: {filename} → Others")

if __name__ == "__main__":
  print("creating folders")
  create_folder()
  print("Renaming files")
  rename_file()
  print(" moving files to designated folders")
  move_files()


