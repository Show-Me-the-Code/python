import os,re
ex = re.split("[\r\n]+",unicode(open(os.path.split(os.path.realpath(__file__))[0]+"/filtered_words.txt").read().decode("GBK")))
Find = re.compile("("+("%s|"*len(ex)%tuple(ex))[:-1]+")")
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
		print Find.sub("**",input)