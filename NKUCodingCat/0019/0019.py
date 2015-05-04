#coding=utf-8
import xlrd, json, os
from lxml import etree
path = os.path.split(os.path.realpath(__file__))[0]+"/"
data = xlrd.open_workbook(path+"numbers.xls")
table = data.sheets()[0]
nrows = table.nrows
Dict = []
for i in range(nrows ):
	Arr = table.row_values(i)
	Dict.append(Arr)
root = etree.Element("root")
child1 = etree.SubElement(root, "numbers")
comm = etree.Comment(u"""数字信息""")
child1.append(comm)
child1.text =unicode(json.dumps(Dict).decode("utf-8"))
tree = etree.ElementTree(root)    
tree.write(path+"numbers.xml ", pretty_print=True, xml_declaration=True, encoding='utf-8')    
