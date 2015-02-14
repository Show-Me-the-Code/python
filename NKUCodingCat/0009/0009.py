import urllib2,re
from lxml import etree
src = urllib2.urlopen("""http://wangwei007.blog.51cto.com/68019/1217082""").read()
for i in etree.HTML(src.decode('utf-8', 'ignore')).xpath(u"//a"):
	print i.attrib["href"]