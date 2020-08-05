#! /usr/bin/python3
# regexsearch.py - opens all .txt files in a folder and searches for any line that matches a user-suplied regular expression. Results should be printed to the screen.

import re, os

regex_user = input('Regex:: ')
reg = re.compile(rf'\b{regex_user}\b')

for filename in os.listdir('.'):
    if filename.endswith('.txt'):
        file = open(filename, 'r')
        content = file.read()
        if reg.search(content) != None:
            print(filename)
        file.close()
    
