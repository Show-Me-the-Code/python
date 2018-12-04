## 第 0014 题

纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：

```
{
	"1":["张三",150,120,100],
	"2":["李四",90,99,95],
	"3":["王五",60,66,68]
}
```

请将上述内容写到 student.xls 文件中

![0014](http://oow6unnib.bkt.clouddn.com/show-me-the-code-0014.jpeg)

>XML 和 Excel 内容相互转换

## 知识点

### xlwt

```
This is a library for developers to use to generate spreadsheet files compatible with Microsoft Excel versions 95 to 2003.
```

**安装：**

```
▶ pip install xlwt
Collecting xlwt
  Downloading xlwt-1.2.0-py2.py3-none-any.whl (99kB)
    100% |████████████████████████████████| 102kB 655kB/s
Installing collected packages: xlwt
Successfully installed xlwt-1.2.0
```

**简单的例子**：[xlwt 1.2.0](https://pypi.python.org/pypi/xlwt)

```
import xlwt
from datetime import datetime

style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
    num_format_str='#,##0.00')
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')

ws.write(0, 0, 1234.56, style0)
ws.write(1, 0, datetime.now(), style1)
ws.write(2, 0, 1)
ws.write(2, 1, 1)
ws.write(2, 2, xlwt.Formula("A3+B3"))

wb.save('example.xls')
```

### API的使用

**第一个类：class xlwt.Workbook.Workbook(encoding='ascii', style_compression=0)**

这是一个表示工作簿及其所有内容的类。 当使用xlwt创建Excel文件时，通常将通过实例化此类的对象来启动。

```
add_sheet(sheetname, cell_overwrite_ok=False)
```

功能：在工作簿中创建工作表

参数：

- sheetname：表名

- cell_overwrite_ok：如果为 `True`，则添加的工作表中的单元格不会在多次写入时引发异常。

```
save(filename_or_stream)
```

功能：将工作簿保存为本机上excel格式的文件

**第二个类：class xlwt.Worksheet.Worksheet(sheetname, parent_book, cell_overwrite_ok=False)**

这是表示工作簿中工作表内容的类。

```
write(r, c, label='', style=<xlwt.Style.XFStyle object>)
```

功能：将单元格写入工作表

参数：

- r: 工作表中应写入单元格的行

- c: 工作表中应写入单元格的列

- label: 要写入的数据

- style: 扩展名，默认为 `.xls`

参考资料：[API Reference](http://xlwt.readthedocs.io/en/latest/api.html)

### 操作excel的几个package

参考资料：[Working with Excel Files in Python](http://www.python-excel.org/)

1、openpyxl

The recommended package for reading and writing Excel 2010 files (ie: .xlsx)

2、xlsxwriter

An alternative package for writing data, formatting information and, in particular, charts in the Excel 2010 format (ie: .xlsx)

3、xlrd

This package is for reading data and formatting information from older Excel files (ie: .xls)

4、xlwt

This package is for writing data and formatting information to older Excel files (ie: .xls)

### json.load

在Python中最常用到的json处理函数通常是json.dumps()和json.loads()，他们和json.dump()和json.load()的区别在于后者是对一个类文件对象（如StringIO）进行写入/读取，而前者是对字符串进行读写，参数都一样。

load()和loads()的工功能是加载json为Python对象。

```
json.load(fp[, encoding[, cls[, object_hook[, parse_float[, parse_int[, parse_constant[, object_pairs_hook[, **kw]]]]]]]])

```
- object_hook：可选函数，将调用任何对象文本解码的结果 
- object_pairs_hook：可选函数，将调用任何的结果对象文本解码成对有序列表 
- parse_float：如果指定，将使用每个 JSON float要解码的字符串调用。默认情况下，这是相当于float(num_str)。这可以用来使用另一种数据类型或解析 JSON float 
- parse_int：如果指定，将使用每个 JSON int 要解码的字符串调用。默认情况下，这是相当于int(num_str)。这可以用来使用另一种数据类型或解析 JSON 整数 
- parse_constant，如果指定，将调用以下字符串之一： ‘-无穷大 ‘， ‘无穷大’、 ‘null’。如果遇到无效的 JSON 格式时引发异常。

loads后是无法保证json_data原始顺序的，如果想要保留原有的顺序，所以就需要用到object_pairs_hook。

### collections模块

Python拥有一些内置的数据类型，比如str, int, list, tuple, dict等， collections模块在这些内置数据类型的基础上，提供了几个额外的数据类型，其中就包括 `OrderedDict` 有序字典

dict这个数据结构由于hash的特性，是无序的，有时候会给我们带来一些麻烦，当要获得一个有序的字典对象时，就可以使用 OrderedDict。

-----
-----
## 第 0016 题

纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：

```
[
	[1, 82, 65535], 
	[20, 90, 13],
	[26, 809, 1024]
]
```

将上述内容写到 numbers.xls 文件中，如下图所示：

![0016](http://oow6unnib.bkt.clouddn.com/show-me-the-code-0016.png)

## json

JSON 语法是 JavaScript 对象表示法语法的子集。

- 数据在名称/值对中
- 数据由逗号分隔
- 花括号保存对象
- 方括号保存数组

名称/值对包括字段名称（在双引号中），后面写一个冒号，然后是值：

```
"firstName" : "John"
```

JSON 对象在花括号中书写, 对象可以包含多个名称/值对：

```
{ "firstName":"John" , "lastName":"Doe" }
```

JSON 数组在方括号中书写, 数组可包含多个对象：

```
{
"employees": [
    { "firstName":"John" , "lastName":"Doe" },
    { "firstName":"Anna" , "lastName":"Smith" },
    { "firstName":"Peter" , "lastName":"Jones" }
  ]
}
```

## 题解

0014和0015都是对象，这里就是简单的数组，所以直接遍历然后写入excel中即可
