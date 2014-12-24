# Source:https://github.com/Show-Me-the-Code/show-me-the-code
# Author:renzongxian
# Date:2014-12-23
# Python 3.4

"""

第 0017 题： 将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中，如
下所示：

<?xml version="1.0" encoding="UTF-8"?>
<root>
<students>
<!--
    学生信息表
    "id" : [名字, 数学, 语文, 英文]
-->
{
    "1" : ["张三", 150, 120, 100],
    "2" : ["李四", 90, 99, 95],
    "3" : ["王五", 60, 66, 68]
}
</students>
</root>

"""

import xlrd
from xml.dom import minidom, Node


def open_xls():
    excel = xlrd.open_workbook("student.xls")
    student_sheet = excel.sheet_by_name("student")
    sheet_content = {}
    for row in range(student_sheet.nrows):
        row_value = student_sheet.row_values(row)
        for i in range(len(row_value)):
            if type(row_value[i]) == float:
                row_value[i] = int(row_value[i])
        sheet_content[str(row+1)] = row_value[1:]
    return sheet_content


def build_xml(content):
    # Create Dom Object
    doc = minidom.Document()
    # Create root tag
    root = doc.createElement('root')
    doc.appendChild(root)
    # Create 'students' tag
    students = doc.createElement('students')
    root.appendChild(students)
    # Create comment element
    students.appendChild(doc.createComment("学生信息表\"id\" : [名字, 数学, 语文, 英文]"))
    # Create text element
    students.appendChild(doc.createTextNode(str(content)))

    # Save the xml file
    student_xml = open('student.xml', 'w')
    student_xml.write(doc.toprettyxml())
    student_xml.close()

if __name__ == '__main__':
    _content = open_xls()
    build_xml(_content)
