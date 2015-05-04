#coding=utf-8
import os,sys,re

def each(path):
	All = []
	for root, dirs, files in os.walk(path):
		for name in files:
			All.append(root+"/"+name)
	return All
def deal(input):
	if os.path.splitext(input)[1] in [".py",".pyw"]:
		total,comment,empty = 0,0,0
		f = open(input,"r")
		in_comment = False
		for line in f:
			total+=1
			if re.findall("\"\"\"$",line):
					if in_comment:
						in_comment = False
					else:
						in_comment = True
			if not re.findall("\S",line):
				empty+=1
			if line[0] == "#" or in_comment:
				comment += 1	
		return total,comment,empty
	else:
		return 0,0,0
		
		
if len(sys.argv)<=1:
	print "The Script will calculate the LOC of the file in "+os.path.split(os.path.realpath(__file__))[0]+"/"
	path = os.path.split(os.path.realpath(__file__))[0]+"/"
else:
	print "calculating the file in "+sys.argv[1]
	if os.path.isdir(sys.argv[1]):
		path = sys.argv[1]
	else:
		print "Path Error! use this script as "+os.path.split(os.path.realpath(__file__))[1]+" [path]"
t,c,e = 0,0,0
for i in each(path):
	t_a,c_a,e_a = deal(i)
	t+=t_a
	c+=c_a
	e+=e_a
print("Total lines: %s. Empty lines: %s. Comment Lines: %s." % (t, e, c))