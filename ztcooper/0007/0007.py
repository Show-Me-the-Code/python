import os

def get_files(start_dir):
	files = []
	for root, dirs, names in os.walk(start_dir):
		for name in names:
			if os.path.splitext(name)[1] == '.py':
				files.append(os.path.join(root,name))
	return files

def cal_lines(files):
	lines = 0
	spaces = 0
	comments = 0
	for file in files:
		with open(file, errors='ignore') as f:
			#因为这里会报错：'gbk' codec can't decode byte 0x90 in position ...
			for each_line in f:
				lines += 1
				if each_line.isspace():
					spaces += 1
				elif each_line.startswith('#'):
					comments += 1
	return (lines, spaces, comments)

if __name__ == '__main__':
	all_files = get_files('E:/Python')
	total_lines = cal_lines(all_files)[0]
	total_spaces = cal_lines(all_files)[1]
	total_comments = cal_lines(all_files)[2]
	print('【.py】源文件%d个，源代码%d行\n' % (len(all_files), total_lines))
	print('目前共累计编写了%d行Python代码，其中包括%d行空行, %d行注释。' % (total_lines, total_spaces, total_comments))