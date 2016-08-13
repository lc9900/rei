#! /usr/bin/env python

import PyPDF2

pdfFileObj = open("sample_statement.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print pdfReader.numPages
outFile = open("output.txt",'a')
raw_list = []
for page in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(page)
    raw_list = pageObj.extractText().split('\n')
    for item in raw_list:
        outFile.write('Item: ')
        outFile.write(item)
        outFile.write('\n')


outFile.close()
pdfFileObj.close()
