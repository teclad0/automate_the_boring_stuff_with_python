#!/usr/bin/python
# filling_in_the_gaps - finds all files with a given prefix in a single folder
# and locates any gaps in the numbering and renames all the later files to
# close this gap

#def missing_gap():

import re, os, sys
prefix_from_user = sys.argv[1].lower()
prefix = re.compile(rf'^({prefix_from_user})(\d\d)\.(.*)')

files_path = []
prex = []
n = []
ext = []

for file in os.listdir('.'):
    if prefix.search(file) != None:
        #prex.append(prefix.search(file).group(0))
        n.append(prefix.search(file).group(2))
        ext.append(prefix.search(file).group(3))
        #print(prex, n, ext)
        #print(file)
#        files_path.append(os.path.relpath(file))
n.sort()
print(n)

#TODO : finds files
#TODO : take out the numbers and check the gap
#TODO : order the files
#TODO : renames files
