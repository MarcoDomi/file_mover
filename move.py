import os

entries = os.scandir("/mnt/c/Users/MarcoDominguez/Downloads")


for entry in entries:
    print(entry.name)
