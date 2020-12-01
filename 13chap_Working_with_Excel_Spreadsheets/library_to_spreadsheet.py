#! python3
#library.py - Operates as library of references on a excel spreadsheet. Enter a title, category, type and link. The title and link can be from clipboard.After finished, will update to a excel spreadsheet.
import openpyxl, os.path, pyperclip

print('Hello, I\'m a library of references.')
title = input('Title? if none, will add from clipboard ')
if (title == ''):
    title=pyperclip.paste()
category = input('Category? ')
type = input('Type? ')
input('Press Enter, link will be added from clipboard')
link = pyperclip.paste()
data = (title,category,type,link)

file_exists=os.path.isfile('library.xlsx')
if file_exists:
    wb = openpyxl.load_workbook('library.xlsx')
    sheet= wb.active
    sheet.append(data)
else:
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet['A1']='TITLE'
    sheet['B1']='CATEGORY'
    sheet['C1']='TYPE'
    sheet['D1']='LINK'
    sheet.append(data)

wb.save('library.xlsx')
