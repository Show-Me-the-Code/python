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
        ws = wb.add_sheet('numbers', cell_overwrite_ok=True)
        for row in range(len(data)):
            for col in range(len(data[row])):
                ws.write(row, col, data[row][col])
        wb.save(outputFile)

if __name__ == '__main__':
    json2excel('numbers.txt', 'numbers.xls')
