import os

def count_lines(file_name):
	line1 = 0
	line2 = 0
	space1 = 0
	space2 = 0
	comment1 = 0
	comment2 = 0
	ext = os.path.splitext(file_name)[1]
	with open(file_name, encoding = 'gbk', errors='ignore') as f:
		for each_line in f:
			if ext == '.cpp':
				line1 += 1
				if not f:
					space1 += 1
				elif f.startwith('//'):
					comment1 += 1
			else:
				line2 += 1
				if not f:
					space2 += 1
				elif f.startwith('#'):
					comment2 += 1

def search_file(start_dir):
	os.chdir(start_dir)
	files = os.listdir(os.curdir)
	for file in files:
		ext = os.path.splitext(file)[1]
		if ext in ['.cpp',  '.py']:
			count_lines(file)

		if os.path.isdir(file):        #判断路径存在且是一个目录
			search_file(file)
			os.chdir(os.pardir)				#返回上一级操作目录

if __name__ == '__main__':
	search_file('E:\\Python')
	print('共写了'+line1+'行C语言代码，其中包括'+space1+'行空格和'+comment1+'行注释。')
	print('共写了'+line2+'行Python代码，其中包括'+space2+'行空格和'+comment2+'行注释。')



