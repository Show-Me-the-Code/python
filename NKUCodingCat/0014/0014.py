#coding=utf-8
import json, xlwt, os
f = open(os.path.split(os.path.realpath(__file__))[0]+"/student.txt")
dict = json.loads(f.read().decode("GBK"))
xls = xlwt.Workbook() 
sheet = xls.add_sheet("student")
for i in range(len(dict.keys())):
	row = i
	col = 0
	sheet.write(row, col, dict.keys()[i])
	for j in (dict[dict.keys()[i]]):
		col+=1
		sheet.write(row, col, j )
xls.save(os.path.split(os.path.realpath(__file__))[0]+"/student.xls")