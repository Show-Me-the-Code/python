from collections import OrderedDict
import xlwt, json

def json2excel(inputFile, outputFile):
    if inputFile.split('.')[1] != 'txt':
        print('please input .txt file!')
        return
    with open(inputFile, 'r') as f:
        data = json.load(f, object_pairs_hook=OrderedDict)
        # 创建实例
        wb = xlwt.Workbook()
        # 添加sheet
        ws = wb.add_sheet('student', cell_overwrite_ok=True)
        # 注意这里的index和后面的i，不要混淆
        for index, (key, values) in enumerate(data.items()):
            #给excel的第一列的每一行添加序号
            ws.write(index, 0, key)

            #给excel的第二列开始的之后每一列的每一行添加数据
            for i, value in enumerate(values):
                ws.write(index, i+1, value)
        wb.save(outputFile)

if __name__ == '__main__':
    json2excel('student.txt', 'student.xls')
