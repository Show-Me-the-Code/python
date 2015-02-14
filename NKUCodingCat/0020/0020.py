#coding=utf-8
import xlrd, json, os
from lxml import etree
path = os.path.split(os.path.realpath(__file__))[0]+"/"
data = xlrd.open_workbook(path+"src.xls")
table = data.sheets()[0]
nrows = table.nrows
Sum = 0
for i in range(1,nrows):
	Arr = table.row_values(i)
	Sum+=int(Arr[3])
print "总计通话时间"+str(Sum)+"秒"