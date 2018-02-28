##0018
#encoding=utf-8
import chardet
from xml.etree.ElementTree import Element,SubElement,Comment,tostring
import pprint

def readXLS(filename):
    import xlrd
    
    data = xlrd.open_workbook(filename,encoding_override='cp1252')
    table = data.sheet_by_name('city')
    s=''
    for row in range(table.nrows):
        s = s + '''"%s":"%s",'''%(table.cell(row,0).value,table.cell(row,1).value)
        
    return s[:-1]


root = Element('root')
comment = Comment(u'city information')
root.append(comment)
child = SubElement(root,'cities')
child.text = readXLS('city.xls')
fw = open('city.xml','w')
fw.write(tostring(root,encoding='utf-8',method='xml'))
#fw.write(tostring(root,encoding='utf-8',method='html'))
#fw.write(tostring(root,encoding='utf-8',method='text'))
fw.close()

