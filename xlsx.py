import openpyxl
from openpyxl.utils import get_column_letter, column_index_from_string

wb = openpyxl.load_workbook('example.xlsx')
sheet = wb['Sheet1']
for row in sheet['A1':'C3']:
    for cell in row:
        print(cell.coordinate, cell.value)
    print('--- END OF ROW ---')

print(list(sheet.columns)[2])
