# 实现有误
import xlrd
from xml.dom import minidom, Node


def gen_xml(root, child, comment, data):
    doc = minidom.Document()
    node_root = doc.createElement(root)
    node_students = doc.createElement(child)
    node_students.appendChild(doc.createComment(comment))
    node_students.appendChild(doc.createTextNode(data))
    node_root.appendChild(node_students)
    doc.appendChild(node_root)
    filename = child + '.xml'
    with open(filename, 'w', encoding='utf-8') as f:
        doc.writexml(f, newl='\n')


def xls_to_xml(filename, comment):
    file = xlrd.open_workbook(filename)
    table = file.sheet_by_name(filename.split('.')[0])
    row = table.nrows
    data = dict()
    for i in range(row):
        data[str(i+1)] = table.row_values(i)[1:]
    print(str(data))
    gen_xml('root', 'students', comment, str(data))

# comment = "学生信息表'id' : [名字, 数学, 语文, 英文]"
# xls_to_xml('student.xls', comment)