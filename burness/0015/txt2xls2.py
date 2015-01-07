#-*- coding: utf-8-*-
import xlwt3
import json


def txt_to_xls(txt_file):
	with open(txt_file,'r') as f:
		# print(f)
		file_content = json.load(f)
		# print(file_content)
		xls_workbook = xlwt3.Workbook()
		xls_sheet = xls_workbook.add_sheet('city')
		style = xlwt3.XFStyle()
		font = xlwt3.Font()
		font.name = '黑体'
		style.font = font
		for i in range(len(file_content)):
			# 写入对应列号
			xls_sheet.write(i, 0, i+1,style)
			json_data = file_content[str(i+1)]
			print(json_data)
			xls_sheet.write(i,1,json_data)
		xls_workbook.save('city.xls')
		



if __name__ == '__main__':
	txt_to_xls('city.txt')