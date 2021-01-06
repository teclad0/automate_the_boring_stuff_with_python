#! python3
# converting_spreadsheeets.py - converts a spreadsheet file into other formats with google spreadsheets

import ezsheets

file_name =input('File ? ')
#TODO: get the file
#TODO: upload the file
ss= ezsheets.upload(file_name)
#TODO: download the file into diferents formats
ss.downloadAsExcel()
ss.downloadAsPDF()
ss.downloadAsODS()
print('Done.')
