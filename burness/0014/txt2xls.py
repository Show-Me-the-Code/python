#-*- coding: utf-8-*-
# xlwt3的参考文档见http://pythonhosted.org//xlwt3/

import xlwt3
import json


def txt_to_xls(txt_file):
	with open(txt_file,'r') as f:
		file_content = json.load(f,encoding = 'utf-8')
		xls_workbook = xlwt3.Workbook(encoding = 'utf-8')
		xls_sheet = xls_workbook.add_sheet('student')
		style = xlwt3.XFStyle()
		font = xlwt3.Font()
		font.name = '黑体'
		style.font = font
		for i in range(len(file_content)):
			# 写入对应列号
			xls_sheet.write(i, 0, i+1,style)
			json_data = file_content[str(i+1)]
			for j in range(len(json_data)):
				xls_sheet.write(i,j+1,json_data[j],style)
		xls_workbook.save('student.xls')
		



if __name__ == '__main__':
	txt_to_xls('student.txt')