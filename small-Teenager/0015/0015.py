import xlsxwriter
import json


def json2xls():
    wb = xlsxwriter.Workbook('city.xls')
    ws = wb.add_worksheet("city")

    with open('city.txt') as f:
        data = json.load(f)

        for i in range(len(data)):
            # print(data[str(i+1)])
            ws.write(i, 0, i + 1)
            ws.write(i, 1, data[str(i + 1)])
    wb.close()


json2xls()
