import os,re
ex = re.split("[\r\n]+",unicode(open(os.path.split(os.path.realpath(__file__))[0]+"/filtered_words.txt").read().decode("GBK")))
while True:
	input = raw_input()
	if input == "":
		break
	else:
		try:
			input = unicode(input)
		except:
			try:
				input = unicode(input.decode("utf-8"))
			except:
				try:
					input = unicode(input.decode("GBK"))
				except:
					raise "Unknown Codec"
		input = re.split("\s+",input)
		Flag = True
		for i in input:
			if i in ex:
				print "Human Rights"
				Flag = False
				break
		if Flag:
			print "Freedom"
			