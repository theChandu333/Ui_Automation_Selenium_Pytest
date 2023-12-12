import xlrd
from utility.config import Config


def read_locators(sheetname):
    workbook = xlrd.open_workbook(Config.locator_path)
    worksheet = workbook.sheet_by_name(sheetname)
    rows = worksheet.get_rows()
    headers = next(rows)
    d = {}
    for row in rows:
        d[row[0].value] = (row[1].value, row[2].value)
    return d


def read_testdata(sheetname):
    workbook = xlrd.open_workbook(Config.testdata_path)
    worksheet = workbook.sheet_by_name(sheetname)
    rows = worksheet.get_rows()
    n_cols = worksheet.ncols
    headers = next(rows)
    data = []
    for row in rows:
        t = ()
        for item in range(n_cols):
            t+=(row[item].value,)
        data.append(t)
    return data


#
print(read_locators("search_products"))
print(read_testdata("search_products"))
