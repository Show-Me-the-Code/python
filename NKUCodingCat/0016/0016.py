#coding=utf-8
import json, xlwt, os
f = open(os.path.split(os.path.realpath(__file__))[0]+"/numbers.txt")
dict = json.loads(f.read().decode("GBK"))
xls = xlwt.Workbook() 
sheet = xls.add_sheet("numbers")
for i in range(len(dict)):
	for j in range(len(dict[i])):
		sheet.write(i , j, dict[i][j])
xls.save(os.path.split(os.path.realpath(__file__))[0]+"/numbers.xls")