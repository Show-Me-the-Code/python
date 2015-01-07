#-*- coding: utf-8-*-
import xlwt3
import json


def txt_to_xls(txt_file):
	with open(txt_file,'r') as f:
		# print(f)
		file_content = json.load(f)
		print(file_content)
		print(file_content[0])
		xls_workbook = xlwt3.Workbook()
		xls_sheet = xls_workbook.add_sheet('numbers')
		style = xlwt3.XFStyle()
		font = xlwt3.Font()
		font.name = '黑体'
		style.font = font
		for i in range(len(file_content)):
			for j in range(len(file_content[i])):
				xls_sheet.write(i,j,file_content[i][j])
		xls_workbook.save('numbers.xls')

if __name__ == '__main__':
	txt_to_xls('numbers.txt')