#! /usr/bin/python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py mcb.pyw save <keyword> - Saves clipboard to keyword.
#       py mcb.pyw <keyword< - Loads keyword to clipboard.
#       py mcb.pyw list - Prints all keywords and values.

import shelve, pyperclip, sys
mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        for keys in mcbShelf.keys():
            print(str(keys) + ' : ' + str(mcbShelf[keys]))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
mcbShelf.close()
