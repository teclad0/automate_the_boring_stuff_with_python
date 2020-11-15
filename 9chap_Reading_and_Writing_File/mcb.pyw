#! /usr/bin/python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py mcb.pyw save <keyword> - Saves clipboard to keyword.
#       py mcb.pyw <keyword< - Loads keyword to clipboard.
#       py mcb.pyw list - Prints all keywords and values.
#       py mcb.pyw delete <keyword> - Deletes keyword

import shelve, pyperclip, sys 
mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3: 
    # Save clipboard content.
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    # Delete keyword.
    elif  sys.argv[1].lower() == 'delete':
        del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        for keys in mcbShelf.keys():
            print(str(keys) + ' : ' + str(mcbShelf[keys]))
    # Deletes all content
    elif sys.argv[1].lower() == 'deletall':
        mcbShelf.clear()
    # Loads content of the keyword to clipboard 
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
     
mcbShelf.close()
