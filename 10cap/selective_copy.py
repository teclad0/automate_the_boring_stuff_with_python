#!/usr/bin/python
# selective_copy.py : walks through a folder tree and searches for files
#   with the file extension given by the user and copies these files to a ne# w folder
# Usage : ./selective_copy.py <extension> <place>

from pathlib import Path
import os,re, shutil, sys

# Extension from command line
ext_from_user = sys.argv[1].lower()
copy_from_user = sys.argv[2].lower() 
print(f'Moving all files with: .{ext_from_user}')
print(f'to dir: {copy_from_user}')

# List with the files to copy
files_path =[]

# Getting the current directory
current_dir = Path.cwd()

copy_dir = os.path.abspath(copy_from_user)

# creates file if it doesn't exist
if not os.path.exists(copy_dir):
    os.makedirs(copy_dir)

# copies files
for filename in os.listdir('.'):
    if filename.endswith(ext_from_user):
        filepath = os.path.join(os.path.abspath(current_dir), filename)
        shutil.copy(filepath, copy_from_user) 


