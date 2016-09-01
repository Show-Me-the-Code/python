##将空行和注释都放到空行

import re

f = open('readme.md')
a = f.readlines()
r1 = re.compile('^"""')
r3 = re.compile('."""$')
r2 = re.compile('^#')
r4 = re.compile('^$')
kong_count = 0
daima_count = 0
flag = 1
### flag 为标志位，是否遇到"""
for line in a:
#	print(line)
	line = line.strip()
	if flag == 1:
		if re.match(r1,line):
			kong_count += 1
			if re.match(r3,line):
				pass
			else:
				flag = -flag
		elif re.match(r2,line):
			kong_count += 1
		elif line == '':
			kong_count += 1
		else:
			daima_count += 1 	
	elif flag == -1:
		kong_count += 1
		if re.match(r1,line):
			flag = -flag
print('空行 %s, 非空行 %s' %(kong_count, daima_count))
