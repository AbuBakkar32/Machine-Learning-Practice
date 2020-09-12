import openpyxl

data = openpyxl.load_workbook('data.xlsx')
print(data.get_sheet_names())
sheet = data.active  # data.get_sheet_by_name('empsheet')

# This script for Read all dat from perticular excel sheeet
# row = sheet.max_row
# col = sheet.max_column
#
#
# for r in range(1, row + 1):
#     for c in range(1, col + 1):
#         print(sheet.cell(row=r, column=c).value, end="         ")
#     print('')


