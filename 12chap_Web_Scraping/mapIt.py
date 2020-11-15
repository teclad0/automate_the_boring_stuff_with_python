#! python3
# mapIt.py - Launches a map in the browser using an address from the command line or clipboard
import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # Get address from command line
    adress = ''.join(sys.argv[1:])
else:
    # Get adress from clipboard
    adress = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + adress)

