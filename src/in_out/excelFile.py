from openpyxl import load_workbook
filename = '/Users/rene.kwak/Private/source/study/python/bjemd.sql'


load_wb = load_workbook("/Users/rene.kwak/Downloads/(포털용)행정동.법정동-매핑_20180518.xlsx", data_only=True)

load_ws = load_wb['법정동-행정동']

all_values = []
linecnt = 0
result = open(filename, 'w')
for row in load_ws.rows:
    linecnt += 1
    emdid = row[5].value
    emdname = row[6].value
    bjemdname = row[10].value
    query = 'insert into pattern_synonym(daumid, keyword, pattern, update_date, value, step) value ("rene.kwak", "%s", "bj_emd", now(), "%s", -1);' %(bjemdname, emdid)
    result.write(query)
    result.write('\r\n')
result.close()