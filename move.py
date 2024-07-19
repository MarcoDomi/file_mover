import os
import shutil
import time
from datetime import datetime
from watchdog.observers.polling import PollingObserver
from watchdog.events import FileSystemEventHandler
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


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f'File {event.src_path} has been modified')

    def on_created(self, event):
        print(f'File {event.src_path} has been created')

    def on_deleted(self, event):
        print(f'File {event.src_path} has been deleted')



if __name__ == "__main__":
    #return_files()
    #file_mover()
    event_handler = MyHandler()
    observer = PollingObserver()
    observer.schedule(event_handler, path=source_path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
