#!/usr/bin/env python

import xlwt3
import json




def loadData(filepath):
    f = open(filepath, "r")
    return json.load(f, encoding = "utf-8")

def writeDataToXls(data):
    xls = xlwt3.Workbook(encoding = "utf-8")
    sheet = xls.add_sheet("student")
    style = xlwt3.XFStyle()
	font = xlwt3.Font()
	font.name = 'ºÚÌå'

    for i in range(len(data)):
        sheet.write(i, 0, i+1,style)
		json_data = data[str(i+1)]
		for j in range(len(json_data)):
			sheet.write(i,j+1,json_data[j],style)
	xls.save('student.xls')


if __name__ == '__main__':
    data = loadData("student.txt")
    writeDataToXls(data)




