#! /usr/bin/python3
# bulletPointAdder.py - Adds Wikipedia bullet poins to the start

import pyperclip

text = pyperclip.paste()
# separate lines and add stars
lines = text.split('\n')
for i in range(len(lines)): #loop through all indexes in the lines list
    lines[i] = '* ' + lines [i] #add star to each string lines list

text = '\n'.join(lines)

pyperclip.copy(text)
