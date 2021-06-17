# 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：
#
# {
# 	"1":["张三",150,120,100],
# 	"2":["李四",90,99,95],
# 	"3":["王五",60,66,68]
# }
# 请将上述内容写到 student.xls 文件中，
import xlsxwriter, json


def json2xls():
    wb = xlsxwriter.Workbook('student.xls')
    ws = wb.add_worksheet("student")

    with open('student.txt') as f:
        data = json.load(f)
        for i in range(len(data)):
            ws.write(i, 0, i + 1)
            json_data = data[str(i + 1)]
            for j in range(len(json_data)):
                ws.write(i, j + 1, json_data[j])
    wb.close()

json2xls()
