#-*- coding: utf-8-*-
import xlrd,codecs
from lxml import etree

def xls_xml(file_name):
	data = []

	excel = xlrd.open_workbook(file_name)
	table = excel.sheet_by_name('numbers')
	# print(table.row_values(0))
	nrows = table.nrows
	for i in range(nrows):
		data.append(table.row_values(i))
	output = codecs.open('numbers.xml','w','utf-8')
	root = etree.Element('root')
	numbers_xml = etree.ElementTree(root)
	numbers = etree.SubElement(root, 'numbers')
	numbers.append(etree.Comment('数字信息'))
	numbers.text = str(data)
	output.write(etree.tounicode(numbers_xml.getroot()))
	output.close()




if __name__ == '__main__':
	xls_xml('numbers.xls')

