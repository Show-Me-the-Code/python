# -*- coding:utf-8 -*-
from xml.dom import minidom
from xlrd import open_workbook
import json
import re

jdict = {}
axls = open_workbook('student.xls')
sheet1 = axls.sheet_by_name('student')
for i in range(3):
    sign = str(sheet1.cell(i,0).value)
    jdict[sign] = []
    for j in range(1,5):
        if j > 1:
            jdict[sign].append(int(sheet1.cell(i,j).value))
        else:
            jdict[sign].append(str(sheet1.cell(i,j).value).decode('gbk'))
#jdata = json.dumps(jdict,indent=4, ensure_ascii=False)
#导入jdata引号会出问题，只得导入jdict，但格式不好看，以下是黑科技，想出这种东西要逼疯我。
s = str(jdict)
s = re.sub('{','{\n\t ',s)
s = re.sub('}','\n}',s)
s = re.sub('],','],\n\t',s)
print s
doc = minidom.Document()
root = doc.createElement('root')
doc.appendChild(root)
students = doc.createElement('students')
comment = doc.createComment(u'\n\t学生信息表\n\t"id" : [名字, 数学, 语文, 英文]\n')
students.appendChild(comment)
students_text = doc.createTextNode(s.decode('unicode_escape'))
students.appendChild(students_text)
root.appendChild(students)
f = open("student.xml", "wb")
f.write(doc.toprettyxml(indent = "", newl = "\n", encoding = "utf-8"))
f.close()

