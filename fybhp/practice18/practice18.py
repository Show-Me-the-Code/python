# -*- coding:utf-8 -*-
from xml.dom import minidom
from xlrd import open_workbook
import re

jdict = {}
axls = open_workbook('city.xls')
sheet1 = axls.sheet_by_name('city')
for i in range(3):
    jdict[str(sheet1.cell(i,0).value)] = str(sheet1.cell(i,1).value).decode('gbk')
s = str(jdict)
s = re.sub('{','{\n\t ',s)
s = re.sub('}','\n}',s)
s = re.sub(',',',\n\t',s)
print s
doc = minidom.Document()
root = doc.createElement('root')
doc.appendChild(root)
students = doc.createElement('citys')
comment = doc.createComment(u'\n\t城市信息\n')
students.appendChild(comment)
students_text = doc.createTextNode(s.decode('unicode_escape'))
students.appendChild(students_text)
root.appendChild(students)
f = open("city.xml", "wb")
f.write(doc.toprettyxml(indent = "", newl = "\n", encoding = "utf-8"))
f.close()