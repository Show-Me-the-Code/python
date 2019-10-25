import xlrd
import xml.dom.minidom as md


def get_xls_data(filename):
     book = xlrd.open_workbook(filename)
     sheet = book.sheet_by_index(0)
     content = {}
     for i in range(sheet.nrows):
         content[i+1] = sheet.row_values(i)[1:]
     return content


def write_to_xml(xlscontent):

    xmlfile = md.Document()　　#创建新xml文件

    root = xmlfile.createElement('root')　　#创建节点
    students = xmlfile.createElement('students')　　#创建节点

    xmlfile.appendChild(root)　　#在文件中添加root节点
    root.appendChild(students)　　#在root下添加students节点

    comment = xmlfile.createComment('学生信息表 "id" : [名字, 数学, 语文, 英文]')　　#创建评论
    students.appendChild(comment)　　#在students标签下添加comment

    xmlcontent = xmlfile.createTextNode(str(xlscontent))　　　　#创建文本节点
    students.appendChild(xmlcontent)　　在students标签下添加文本内容

    with open('students.xml', 'wb') as f:
        f.write(xmlfile.toprettyxml(encoding = 'utf-8'))　　#写入文件


write_to_xml(get_xls_data('students.xls'))
