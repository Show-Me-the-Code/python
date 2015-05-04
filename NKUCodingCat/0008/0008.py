#coding=utf-8
#参考http://blog.csdn.net/gzlaiyonghao/article/details/1741185和http://www.cnblogs.com/jasondan/p/3497757.html的算法思路
#但是第二篇的政治观点并不认同
from __future__ import division
import re,urllib2
import HTMLParser
from lxml import etree
html_parser = HTMLParser.HTMLParser()
res = urllib2.urlopen("""http://www.cnblogs.com/jasondan/p/3497757.html""").read()
D = etree.HTML(res.decode('utf-8', 'ignore'))
F = D.xpath(u"//script")
for i in F:
	i.text = ""
res = etree.tostring(D)
res = re.sub("<[^>]>",">\n",res)
res = re.split("[\r\n]+",res)

for line in res:
	if not line:
		continue
	con =  re.sub(("<[^>]*>"),"",line)
	if len(con)/len(line)>0.5:
		print (html_parser.unescape(con)).encode("GBK","ignore")