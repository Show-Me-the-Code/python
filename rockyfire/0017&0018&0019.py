def open_excel(file='student.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception, e:
        print
        str(e)

def excel_table_by_index(file='student.xls', colname_index=0, by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows
    ncols=table.ncols
    print (ncols)
    colnames = table.row_values(colname_index)
    list = []
    for rownum in range(nrows):
        # 当前行是否有数据
        row = table.row_values(rownum)
        if row:
            app = {}
            # for i in range(len(colnames)):
            for i in range(ncols):
                app[str(i)] = row[i]
            list.append(app)
    return list

info_fight_monster_xml=etree.ElementTree(etree.Element("root"))
student_xml = etree.SubElement(info_fight_monster_xml.getroot(), 'student')

if __name__ == '__main__':
    tables=excel_table_by_index()
    list=[]
    for row in tables:
        list_key  =[v for k,v in row.items() if k == "0"]
        list_value=[v for k,v in row.items() if k != "0"]
        list.append("".join(list_key)+":"+",".join(list_value)+'\n')
    student_xml.text="".join(list)

    output=codecs.open('student.xml','w','utf-8')
    output.write(etree.tounicode(info_fight_monster_xml.getroot()))
    output.close()
