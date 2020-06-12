#! /usr/bin/python
# phoneAndEmail.py - finds phone numbers and email addresses on the clipboard

import pyperclip
import re
# regexes:
phoneRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?      #area code, ? makes optional
        (\s|-|\.)?              #separator
        (\d{3})                   #first 3 digits
        (\s|-|\.)               #separator
        (\d{4})                   #last 4 digits
        (\s*(ext|x|ext.)\s*\d{2,5})?  #extension
        )''',re.VERBOSE)

emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+       #is one or more ch
        @
        [a-zA-Z0-9.-]+
        (\.[a-zA-Z]{2,4})
        )''',re.VERBOSE)

#find matches in clipboard text
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1],groups[3],groups[5]])
    if groups[7] !='':
        phoneNum += ' x' + groups[7]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('nothing found')


