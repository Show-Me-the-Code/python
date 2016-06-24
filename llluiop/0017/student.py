#!/usr/bin/env python
#-*- coding: utf-8-*-

import xlrd, codecs, json
from lxml import etree


def load_data(file_path):
    xls = xlrd.open_workbook(file_path)
    sheet = xls.sheet_by_index(0)

    data = {}
    for i in range(sheet.nrows):
        data[str(sheet.row_values(i)[0])] = str(sheet.row_values(i)[1].encode("utf-8"))

    return json.dumps(data, encoding="UTF-8", ensure_ascii=False)

def write_data_to_xls(data):
    xml = codecs.open("student.xml", "w", encoding="utf-8")

    ele_root = etree.Element("root")
    xml_root = etree.ElementTree(ele_root)
    xml_student = etree.SubElement(ele_root, "students")
    #xml_student.append(etree.Comment(u'ѧ����Ϣ��\n\"id\": [���֣���ѧ�����ģ�Ӣ��]'))
    xml_student.text = str(data)

    xml.write(etree.tounicode(xml_root.getroot()))
    xml.close()


if __name__ == '__main__':
    data = load_data("student.xls")
    write_data_to_xls(data)




