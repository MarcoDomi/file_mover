import os
import shutil
import time
import sys
from watchdog.observers.polling import PollingObserver
from watchdog.events import FileSystemEventHandler


valid_extensions = [".jpg", ".jpeg", ".png", ".json"]
source_path = "/mnt/c/Users/MarcoDominguez/Downloads"

if len(sys.argv) == 1: 
    dest_path = "/home/marcodom/Downloads" #if no dest_path is provided in terminal set dest_path to this directory
else:
    dest_path = sys.argv[1]

def return_files(): #used to return files from dest_path back to source_path
    with os.scandir(dest_path) as entries:
        for entry in entries:
            shutil.move(entry, source_path)

def min_since_file_modified(file): #minutes since file was modified
    c = os.path.getmtime(file)
    curr = time.time()
    seconds_per_min = 60.0
    time_elapse = (curr - c) / seconds_per_min

    return time_elapse

def is_valid_extension(file_name):
    index = file_name.find('.')
    file_extension = file_name[index:]
    is_valid = file_extension in valid_extensions
    return is_valid


def file_mover():  # if file has a valid extension and the modified time was no more than 10 minutes ago then move file to dest_path
    valid_min_elapsed = 10.0 #10 minutes
    with os.scandir(source_path) as entries:
        for entry in entries:
            if is_valid_extension(entry.name) and min_since_file_modified(source_path + '/' + entry.name) < valid_min_elapsed: 
                shutil.move(entry, dest_path)


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f'File {event.src_path} has been modified')

    def on_created(self, event):
        print(f'File {event.src_path} has been created')
        file_mover()

    def on_deleted(self, event):
        print(f'File {event.src_path} has been deleted')


if __name__ == "__main__":
    event_handler = MyHandler()
    observer = PollingObserver() #use polling observer b/c source_path is on windows and dest_path is on wsl
    observer.schedule(event_handler, path=source_path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
