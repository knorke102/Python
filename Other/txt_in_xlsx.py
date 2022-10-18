from openpyxl import Workbook

book = Workbook()
sheet = book.active

r = 1

with open('artifact.txt', encoding='utf-8', mode='r') as file:
    for i in file:
        sheet.cell(row=r, column=2).value = i
        r += 1

book.save('test.xlsx')
