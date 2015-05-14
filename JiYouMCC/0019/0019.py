# -*- coding: utf-8 -*-
import xlrd
from xml.dom.minidom import Document
from xml.etree.ElementTree import Comment, Element
import json

infos = []
info_file = xlrd.open_workbook('numbers.xls')
info_table = info_file.sheets()[0]
row_count = info_table.nrows
doc = Document()
root = doc.createElement('root')
doc.appendChild(root)
numbers = doc.createElement('numbers')
for row in range(row_count):
    number = doc.createElement('number')
    col1 = doc.createElement('column')
    col1.appendChild(doc.createTextNode('%d' % info_table.cell(row, 0).value))
    number.appendChild(col1)
    col2 = doc.createElement('column')
    col2.appendChild(doc.createTextNode('%d' % info_table.cell(row, 1).value))
    number.appendChild(col2)
    col3 = doc.createElement('column')
    col3.appendChild(doc.createTextNode('%d' % info_table.cell(row, 2).value))
    number.appendChild(col3)
    numbers.appendChild(number)
root.appendChild(numbers)
file = open('numbers.xml', 'w')
file.write(doc.toprettyxml(indent=''))
file.close()
