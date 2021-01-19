#! python3
# inveterd_pdf.py - inverts the order of pages of a pdf document

import PyPDF2, os

pdf_name = input('Name ?')

pdfFileObj=open(pdf_name, 'rb')
pdfWriter = PyPDF2.PdfFileWriter()

pdfReader=PyPDF2.PdfFileReader(pdfFileObj)

for pageNum in range(pdfReader.numPages - 1, -1, -1):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

pdfOutput = open('result.pdf','wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
