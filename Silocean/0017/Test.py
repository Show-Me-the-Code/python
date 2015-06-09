
# -*-coding:utf-8-*-

__author__ = 'Tracy'
import xlrd, re, json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# xlrd.Book.encoding = 'gbk'
with xlrd.open_workbook('student.xls') as file:
    table = file.sheet_by_index(0)

rows = table.nrows
cols = table.ncols

dic = {}

content = '<?xml version="1.0" encoding="UTF-8"?>\n<root>\n<students>\n<!--\n    学生信息表\n    "id" : [名字, 数学, 语文, 英文]\n-->\n'

for row in range(rows):
    stu = table.row_values(row)
    list = []
    for x in range(len(stu)-1):
        list.append(stu[x+1])
        # print(isinstance(stu[x+1],unicode)) # 判断是否是unicode编码
    dic[stu[0]] = list

s = json.dumps(dic, indent=4, ensure_ascii=False)

content = content + s + '\n</students>\n</root>'
with open('student.xml', 'w') as f:
    f.write(content)


