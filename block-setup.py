import os

# Find Valid Folders
valid_folders = []
for folder in [x[0] for x in os.walk('.')]:
    if folder.count('/') == 1 and folder.count('.') == 1:
        valid_folders.append(folder[2:])

# Find tags in the block.html
