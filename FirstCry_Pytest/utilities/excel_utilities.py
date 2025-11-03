import openpyxl, os

def get_testdata(excelpath='testdata.xlsx', sheetname='Sheet1'):
    if not os.path.exists(excelpath):
        raise FileNotFoundError(f"Test data file not found: {excelpath}")
    wb = openpyxl.load_workbook(excelpath)
    sheet = wb[sheetname]
    headers = [cell.value for cell in sheet[1]]
    data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        item = {}
        for k, v in zip(headers, row):
            item[k] = v
        data.append(item)
    return data
