import gspread

api_access = gspread.service_account(filename='quick.json')
sheet = api_access.open_by_key('1auSrclKnO7PW4_Dy2zAi_L59AsOdc4PBJPWRVoFD5kU')

ws = sheet.sheet1
#result = ws.get_all_records()
#result = ws.get_all_values()
#result = ws.col_values(1)
# result = ws.get('A2:C2')
# add = [100, 1000, 10000]
# ws.append_row(add)
# ws.delete_columns(1)
# ws.delete_row(1)



