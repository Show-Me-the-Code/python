import collections,re
import sys
def cal(filename = 'in.txt'):
	print 'now processing:' + filename + '......'
	f = open(filename,'r')
	data = f.read()
	dic = collections.defaultdict(lambda :0)
	data = re.sub(r'[\W\d]',' ',data)
	data = data.lower()
	datalist = data.split(' ')
	for item in datalist:
		dic[item] += 1
	del dic['']
	return dic
try:
	print sorted(cal().items())
except:
	print 'no input file'
