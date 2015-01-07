#-*- coding: utf-8-*-
import xlrd,codecs
from lxml import etree

def xls_xml(file_name):
	data = {}

	excel = xlrd.open_workbook(file_name)
	table = excel.sheet_by_name('student')
	# print(table.row_values(0))
	nrows = table.nrows
	for i in range(nrows):
		key = str(int(table.row_values(i)[0]))
		value = str(table.row_values(i)[1:])
		data[key] = value

	output = codecs.open('students.xml','w','utf-8')
	root = etree.Element('root')
	students_xml = etree.ElementTree(root)
	students = etree.SubElement(root, 'students')
	students.append(etree.Comment('学生信息表\n\"id\": [名字，数学，语文，英语]'))
	students.text = str(data)
	output.write(etree.tounicode(students_xml.getroot()))
	output.close()




if __name__ == '__main__':
	xls_xml('student.xls')

