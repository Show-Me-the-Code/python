#!/bin/env python
# -*- coding: utf-8 -*- 

#使用Python3语法，实现一个将不引入第三方库实现XML-->JSON 思路的例子
#来自于：http://blog.csdn.net/laoyaotask/article/details/41384719
#使用 $python3 xml2json 执行该脚本，我也准备开始逐渐尝试用Python3的语法来写Python程序了，以前不知道命令行可以分别跑Python2和Python3
#默认还是建议设置为使用Python2，因为很多库和开源程序都是基于Python2的规范编写的

from xml.etree import ElementTree as et;
import json

#从xml文件读取结点 转换为json格式，并保存到文件中
print('read node from xmlfile, transfer them to json, and save into jsonFile:')
root=et.parse("testXml.xml");
#我习惯加个横线，虽然不知道为什么作者的代码中不加也能用
f=open('testJson.json','a',encoding="utf-8");
for each in root.getiterator("person"):
    tempDict=each.attrib
    for childNode in each.getchildren():
        tempDict[childNode.tag]=childNode.text
    tempJson=json.dumps(tempDict,ensure_ascii=False)
    print(tempJson)
    f.write(tempJson+"\n");
f.close()

#从json文件中读取，并打印
print('read json from jsonfile:')
#加了横线
for eachJson in open('testJson.json','r',encoding='utf-8'):
    tempStr=json.loads(eachJson);
    print(tempStr)
