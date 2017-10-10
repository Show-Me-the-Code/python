# -*- coding: utf-8 -*-
"""
 将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中，如

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
import xlwt, json
from collections import OrderedDict

with open('source/0014/student.txt', 'r') as f:
    L = []
    L.append(r"""
<?xml version="1.0" encoding="UTF-8"?>
<root>
<students>
<!--
	学生信息表
	"id" : [名字, 数学, 语文, 英文]
-->
    """)
    L.append(f.read())
    L.append(r"""
</students>
</root>
    """)
    with open('source/0014/student.xml', 'w') as s:
        s.write(''.join(L))
