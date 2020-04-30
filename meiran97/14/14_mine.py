'''
纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：
{
	"1":["张三",150,120,100],
	"2":["李四",90,99,95],
	"3":["王五",60,66,68]
}
请将上述内容写到 student.xls 文件中，如下图所示：
'''
# 学习了json格式
# 学习了xlwt
import json, xlwt

text = '''
{
	"1":["张三",150,120,100],
	"2":["李四",90,99,95],
	"3":["王五",60,66,68]
}
'''
text_json = json.loads(text)
print(text_json)

wb = xlwt.Workbook()
ws = wb.add_sheet('numbers', cell_overwrite_ok=True)
for i, (k, v) in enumerate(text_json.items()):
    ws.write(i, 0, k)
    for i2, value in enumerate(v):
        col = i2 + 1
        ws.write(i, col, value)
wb.save('students.xls')
