#encoding=utf-8
##0017
import chardet
from xml.etree.ElementTree import Element,SubElement,Comment,tostring
import pprint

def readXLS(filename):
    import xlrd
    
    data = xlrd.open_workbook(filename,encoding_override='cp1252')
    table = data.sheet_by_name('student')
    s=''
    for row in range(table.nrows):
        s = s + '''"%s":["%s",%d,%d,%d],'''%(table.cell(row,0).value,table.cell(row,1).value,\
                                             table.cell(row,2).value,table.cell(row,3).value,table.cell(row,4).value)
        
    return s[:-1]


root = Element('root')
comment = Comment(u'学生信息表\n"id":[名字，数学，语文，英语]')
root.append(comment)
child = SubElement(root,'students')
child.text = readXLS('student.xls')
fw = open('student.xml','w')
fw.write(tostring(root,encoding='utf-8',method='xml'))
#fw.write(tostring(root,encoding='utf-8',method='html'))
#fw.write(tostring(root,encoding='utf-8',method='text'))
fw.close()
