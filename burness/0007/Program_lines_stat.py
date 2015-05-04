#-*- coding: utf-8 -*-
'''
123123
123
'''

# 统计包括c/c++,python程序代码行、注释行

# 建字典，保存对应的程序语言和后缀、单行注释符、多行注释符
import pdb
# 扩展其他程序可以在这里加入
lan_postfix={'python':'.py','c':'.c'}
lan_comment={'python':'#','c':'//'}
# 解决多行注释 如python中的'''
multi_comment_start={'python':'\'\'\'','c':'/*'}
multi_comment_end={'python':'\'\'\'','c':'*/'}
def stat_lines(file_name,file_type):
	import re
	is_comment=False
	stat_result={'comment':0,'content':0,'null_line':0}
	with open(file_name,'rt',encoding='utf-8') as f:
		if file_name.endswith(lan_postfix[file_type]):
			for line in f.readlines():
				# pdb.set_trace()
				line_next=line.lstrip()
				# fuck a bug here in c multi comment
				if not is_comment and line_next.startswith(multi_comment_start[file_type]):
					is_comment= True
					stat_result['comment']+=1
					continue
				if line_next.startswith(multi_comment_end[file_type]):
					is_comment=False
					stat_result['comment']+=1
				# print(line)
				# print(line_next)
				if not line.split():
					stat_result['null_line']+=1
				elif line_next.startswith(lan_comment[file_type]) or is_comment:
					stat_result['comment']+=1
				else:
					stat_result['content']+=1
	return stat_result


def main():
	import os
	import pdb	
	c_sum_stat={'comment':0,'content':0,'null_line':0}
	python_sum_stat={'comment':0,'content':0,'null_line':0}
	for file in os.listdir('.'):
		if file.endswith('.c') or file.endswith('.cpp'):
			# c_stat应该是一个字典，keys包括comment，content，null_line
			# pdb.set_trace()
			c_stat=stat_lines(file,'c')
			c_sum_stat['comment']+=c_stat['comment']
			c_sum_stat['content']+=c_stat['content']
			c_sum_stat['null_line']+=c_stat['null_line']
		elif file.endswith('.py'):
			python_stat=stat_lines(file,'python')
			python_sum_stat['comment']+=python_stat['comment']
			python_sum_stat['content']+=python_stat['content']
			python_sum_stat['null_line']+=python_stat['null_line']
	print('C code lines:{0}\nC comment lines:{1}\nC null_line lines:{2}'.format(c_sum_stat['content'],\
		c_sum_stat['comment'],c_sum_stat['null_line']))

	print('Python code lines:{0}\nPython comment lines:{1}\nPython null_line lines:{2}'.format(python_sum_stat['content'],\
		python_sum_stat['comment'],python_sum_stat['null_line']))


if __name__=='__main__':
	main()
