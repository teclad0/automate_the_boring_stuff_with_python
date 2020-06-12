#!/usr/bin/python
# selective_copy.py : walks through a folder tree and searches for files
#   with the file extension given by the user and copies these file#   s to a  new folder.
# Usage : ./selective_copy.py <extension> <place>

from pathlib import Path
import os,re, shutil, sys

# Extension from command line
ext_from_user = sys.argv[1].lower()
copy_dir = sys.argv[2].lower() 
print(f'Moving all files with: .{ext_from_user}')
print(f'to dir: {copy_dir}')

# Extension regex
ext = re.compile(rf'.{ext_from_user}')

# List with the files to copy
files_path =[]

# Getting the current directory
current_dir = Path.cwd()

# Getting all the files inside the current directory
for filename in os.listdir('.'):
    if ext.search(filename) != None:
        files_path.append(os.path.abspath(filename))

# Copying the files
for file in files_path:
    shutil.copy(file, current_dir / copy_dir)

