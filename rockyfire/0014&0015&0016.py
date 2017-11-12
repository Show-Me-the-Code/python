#python2.7
from lxml import etree
import xlwt

def parse_txt(ws,fs,row=0):
    for i in fs:
        # 列
        col=0
        for index,value in enumerate(i):
            ws.write(row, col, value)
            col +=1
        # 行
        row +=1
    yield row

def student_data(f):
    fs = []
    for f_lines in f.readlines():
        f_line = f_lines.strip()
        # 0016
        booleans = f_line == "[" or f_line == "]"

        booleans = f_line == "{" or f_line == "}"
        if booleans == False:
            line_list = [i for i in f_line.split(":")[0] if i != '"']
            line_data = [i for i in f_line.split(":")[1].rstrip(",").strip("[|]").split(",")]
            # 0015
            line_data = [i for i in f_line.split(":")[1]]
            # 0016
            line_list = [i for i in f_line.restrip(",").strip("[|]").split(",")]

            line_list.extend(line_data)
            fs.append(line_list)
    parse_txt(ws, fs).next()




if __name__ == "__main__":
    wb = xlwt.Workbook(encoding='utf-8')
    # 新建一个sheet
    ws = wb.add_sheet('student',cell_overwrite_ok=True)
    with open("student.txt") as f:
        student_data(f)
    # 保存文件
    wb.save("student.xls")

