'''
第 0016 题： 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：
[
	[1, 82, 65535],
	[20, 90, 13],
	[26, 809, 1024]
]
请将上述内容写到 numbers.xls 文件中，如下图所示：
'''

import json, xlwt
text = '''
[
	[1, 82, 65535], 
	[20, 90, 13],
	[26, 809, 1024]
]
'''

data = json.loads(text)
wb = xlwt.Workbook()
ws = wb.add_sheet('numbers', cell_overwrite_ok=True)
print(data)
for i, lst in enumerate(data):
    for i2, v in enumerate(lst):
        ws.write(i, i2, v)
wb.save('numbers.xls')