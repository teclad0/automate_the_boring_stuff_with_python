#! /usr/bin/python3
# bulletPointAdder.py - Adds Wikipedia bullet poins to the start

import pyperclip

text = pyperclip.paste()
# separate lines and add stars
text = text.upper()

pyperclip.copy(text)
