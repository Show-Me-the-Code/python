## xls2xml.py （读入xls内容，转化为xml保存）

1.	xls数据读入问题：读入xls文件，excel = xlrd.open_workbook(file_name);选定对应sheet，table = excel.sheet_by_name('student');按行读入指定表内容for i in range(nrows): print table.row_values(i)。
2.	xml问题：

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

其中root：root = etree.Element("root")；students:students = etree.SubElement(root, "students");comment:student.append(etree.Comment('some comment'));text：students.text = "TEXT"即为xls中读取的内容.
3.  保存问题：output = codecs.open('students.xml','w','utf-8');students_xml = etree.ElementTree(root);output.write(etree.tounicode(students_xml.getroot()));output.close()
