#! python3
# mistakes_spreadsheet.py - finds mistakes in the Bean Count spreadsheet
import ezsheets, traceback

try:
    ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')
    rows = ss[0].getRows()

    for i in range(1,ss[0].rowCount):
        if int(rows[i][0]) * int(rows[i][1]) != int(rows[i][2]):
            print(f'false em {i} ')

except:
    print('Valores vazios')
