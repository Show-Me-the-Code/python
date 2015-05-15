#coding=utf-8
import json, xlwt, os
f = open(os.path.split(os.path.realpath(__file__))[0]+"/city.txt")
dict = json.loads(f.read().decode("GBK"))
xls = xlwt.Workbook() 
sheet = xls.add_sheet("city")
for i in range(len(dict.keys())):
	row = i
	col = 0
	sheet.write(row, col, dict.keys()[i])
	sheet.write(row, col+1, dict[dict.keys()[i]])
xls.save(os.path.split(os.path.realpath(__file__))[0]+"/city.xls")