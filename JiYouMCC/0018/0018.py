# -*- coding: utf-8 -*-
import xlrd
from xml.dom.minidom import Document
from xml.etree.ElementTree import Comment, Element
import json

infos = []
info_file = xlrd.open_workbook('city.xls')
info_table = info_file.sheets()[0]
row_count = info_table.nrows
doc = Document()
root = doc.createElement('root')
doc.appendChild(root)
citys = doc.createElement('citys')
for row in range(row_count):
    city = doc.createElement('city')
    city.setAttribute('id', '%d' % info_table.cell(row, 0).value)
    city.appendChild(
        doc.createTextNode('%s' % info_table.cell(row, 1).value.encode('utf-8')))
    citys.appendChild(city)
root.appendChild(citys)
file = open('citys.xml', 'w')
file.write(doc.toprettyxml(indent=''))
file.close()
