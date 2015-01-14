import urllib2
from HTMLParser import HTMLParser
from traceback import print_exc
from sys import stderr

class _DeHTMLParser(HTMLParser):
	'''
	利用HTMLParse来解析网页元素
	'''
	def __init__(self):
		HTMLParser.__init__(self)
		self.img_links = []

	def handle_starttag(self, tag, attrs):
		if tag == 'img':
			# print(attrs)
			try:
				if ('pic_type','0') in attrs:
					for name, value in attrs:
						if name == 'src':
							self.img_links.append(value)
			except Exception as e:
				print(e)


		return self.img_links


def dehtml(text):
	try:
		parser = _DeHTMLParser()
		parser.feed(text)
		parser.close()
		return parser.img_links
	except:
		print_exc(file=stderr)
		return text


def main():
	html = urllib2.urlopen('http://tieba.baidu.com/p/2166231880')
	content = html.read()
	print(dehtml(content))
	i = 0
	for img_list in dehtml(content):
		img_content = urllib2.urlopen(img_list).read()
		path_name = str(i)+'.jpg'
		with open(path_name,'wb') as f:
			f.write(img_content)
		i+=1

if __name__ == '__main__':
	main()