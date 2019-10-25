# -*- coding:utf-8 -*-
from xml.dom import minidom
from xlrd import open_workbook
import re

jdict = []
axls = open_workbook('numbers.xls')
sheet1 = axls.sheet_by_name('numbers')
for i in range(3):
    jdict.append([])
    for j in range(3):
        jdict[i].append(int(sheet1.cell(i,j).value))
s = str(jdict)
print s
s = re.sub('\[\[','[\n\t [',s)
s = re.sub('\]\]',']\n]',s)
s = re.sub('],','],\n\t',s)
print s
doc = minidom.Document()
root = doc.createElement('root')
doc.appendChild(root)
students = doc.createElement('numbers')
comment = doc.createComment(u'\n\t数字信息\n')
students.appendChild(comment)
students_text = doc.createTextNode(s)
students.appendChild(students_text)
root.appendChild(students)
f = open("numbers.xml", "wb")
f.write(doc.toprettyxml(indent = "", newl = "\n", encoding = "utf-8"))
f.close()