import xlrd
file_location = ("A:\InvoiceDataset\PracticeBook.xlsx")
workbook=xlrd.open_workbook(file_location)
inputsheet=workbook.sheet_by_index(0)

"""for row in range(inputsheet.nrows):
    print (inputsheet.cell_value(row,3))"""
inputsheetdata=[[inputsheet.cell_value(r,c) for c in range (inputsheet.ncols)] for r in range(inputsheet.nrows)]
for invoiceID in range (833229,932255):
    invoiceIDstart=('0'+ str(invoiceID))
    outputlist=[(inputsheetdata[product][3]) for product in range(inputsheet.nrows) if inputsheetdata[product][1]==invoiceIDstart]
    print (invoiceIDstart,'=',outputlist)
