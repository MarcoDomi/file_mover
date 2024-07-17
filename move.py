import os
import shutil
from datetime import datetime
# TODO remove testfolder directory later

valid_extensions = [".jpg", ".jpeg", ".png"]
source_path = "/mnt/c/Users/MarcoDominguez/Downloads"
dest_path = "/home/marcodom/repos/file_mover/testfolder" #will change later

def return_files(): #will delete later
    with os.scandir(dest_path) as entries:
        for entry in entries:
            shutil.move(entry, source_path)

def is_valid_extension(file_name):
    index = file_name.find('.')
    file_extension = file_name[index:]
    is_valid = file_extension in valid_extensions
    return is_valid

def file_mover():
    with os.scandir(source_path) as entries:
        for entry in entries:
            if is_valid_extension(entry.name):
                shutil.move(entry, dest_path)

#return_files()
file_mover()
