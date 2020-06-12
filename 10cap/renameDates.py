#! /usr/bin/python3
# renameDates.py - Renames filenames with American MM-DD-YYY#                  Y date format
#                  to Brazilian DD-MM-YYYY.

import shutil, os, re
#Create a regex that matches files with the American date format.
datePattern = re.compile(r"""^(.*?) # all text berfode the date
        ((0|1)?\d)-  # one or two digits for he month
        ((0|1|2|3)?\d)- # one or two digits for the day
        ((19|20)\d\d)  #four digits for the year
        (.*?)$  # all text after the date
        """, re.VERBOSE)

# Loop over the files in the workind directory.
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
    # Skip files without a date.
    if mo == None:
        continue
    # Get the different aprts of the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)
    # form the european-style filename
    brFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    brFilename = os.path.join(absWorkingDir, brFilename)
    # Rename the files
    #print(f'Renaming "{amerFilename}" to "{brFilename}"...')
    shutil.move(amerFilename, brFilename) 

