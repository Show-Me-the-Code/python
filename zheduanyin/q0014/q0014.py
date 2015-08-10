# 写入excel
import json
import xlwt
import os

def open_json(path):
    try:
        return json.loads(open(path).read())
    except Exception as e:
        print(e)


def copy_json_into_excel(json_path):
    print('- start running..')
    excel_path = os.path.splitext(json_path)[0] + '.xls'
    sheet_name = os.path.splitext(os.path.basename(json_path))[0]
    json_data = open_json(json_path)
    book = xlwt.Workbook()
    sheet1 = book.add_sheet(sheet_name)

    if isinstance(json_data, dict):
        for k, row in zip(sorted(json_data), range(len(json_data))):
            print('\tline', row)
            print('\t\tcol', 0)
            sheet1.write(row, 0, k)
            if isinstance(json_data[k], list):
                for col in range(1, len(json_data[k]) + 1):
                    print('\t\tcol', col)
                    sheet1.write(row, col, json_data[k][col - 1])
            elif isinstance(json_data[k], str):
                print('\t\tcol', 1)
                sheet1.write(row, 1, json_data[k])
    elif isinstance(json_data, list):
        for row in range(len(json_data)):
            print('\tline', row)
            for col, item in enumerate(json_data[row]):
                print('\t\tcol', col)
                sheet1.write(row, col, item)

    book.save(excel_path)
    print('- done..')
    return json_data

if __name__ == '__main__':
    data = copy_json_into_excel('student.txt')
