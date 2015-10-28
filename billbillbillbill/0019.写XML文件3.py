#!/usr/bin/env python
#coding: utf-8
import json
import xlrd 
from collections import OrderedDict
import xml.dom.minidom as minidom
import HTMLParser
# xml.sax.saxutils中的unescape只能Unescape把字符串中的 '&amp;', '&lt;', and '&gt;'，对于其他就无力了

# 存放文件的路径
filepath = '/home/bill/Desktop/numbers.xls'
xmlpath = '/home/bill/Desktop/numbers.xml'
comment = '''
    <!--
        数字信息
    -->
'''

def readDataToJson():
    # 打开表格
    data = xlrd.open_workbook(filepath)
    sheet = data.sheet_by_index(0)
    # 注意要使用orderdict读取，确保元素位置一致
    d = []
    for i in range(sheet.nrows):
        # 读一行，存放到dict中
        values = map(lambda x: x.encode('UTF8') if isinstance(x, unicode) else x, sheet.row_values(i))
        d.append(values)
    return d

class MakeXml():
    def __init__(self, xmlpath):
        self.xmlpath = xmlpath
        self.dom = minidom.DOMImplementation().createDocument(None, 'root', None)
        self.root = self.dom.documentElement

    def creat_node(self, node_name, node_text=None, comment=None):
        if None == node_text:
            newNode = self.dom.createElement(node_name)
        else:
            if None != comment:
                newText = self.dom.createTextNode(comment+node_text)
            else:
                newText = self.dom.createTextNode(node_text)
            newNode = self.dom.createElement(node_name)
            newNode.appendChild(newText)
        return newNode

    def add_child(self, item, comment=None):
        # 注意中文问题
        new_node = self.creat_node('numbers', json.dumps(item, indent=4, ensure_ascii=False, encoding="utf-8", separators=(',', ': ')), comment)
        self.root.appendChild(new_node)

    def save(self):
        # 直接writexml会转义掉字符
        # Node.toxml会返回字符串格式的DOM
        with open(self.xmlpath, 'w') as f:
            html_parser = HTMLParser.HTMLParser()
            tranform = html_parser.unescape(self.dom.toxml().decode('utf-8'))
            f.write(tranform.encode('utf-8'))

if __name__ =="__main__":
    newxml = MakeXml(xmlpath)
    newxml.add_child(readDataToJson(), comment)
    newxml.save()
