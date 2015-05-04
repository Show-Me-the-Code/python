#coding=utf-8
import xlrd, json, os
from lxml import etree
path = os.path.split(os.path.realpath(__file__))[0]+"/"
data = xlrd.open_workbook(path+"city.xls")
table = data.sheets()[0]
nrows = table.nrows
Dict = {}
for i in range(nrows ):
	Arr = table.row_values(i)
	Dict[Arr[0]] = Arr[1]
root = etree.Element("root")
child1 = etree.SubElement(root, "city")
comm = etree.Comment(u"""城市信息""")
child1.append(comm)
child1.text =unicode(json.dumps(Dict))
tree = etree.ElementTree(root)    
tree.write(path+"city.xml ", pretty_print=True, xml_declaration=True, encoding='utf-8')    
