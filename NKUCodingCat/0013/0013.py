import requests,os,re,urllib
from lxml import etree
src = requests.get("""http://tieba.baidu.com/p/2166231880""").content
path = os.path.split(os.path.realpath(__file__))[0]+"/img/"
for i in etree.HTML(src.decode('utf-8', 'ignore')).xpath(u"//img"):
	url = i.attrib["src"]
	proto, rest = urllib.splittype(url)  
	host, rest = urllib.splithost(rest)  
	if host == "imgsrc.baidu.com":
		urllib.urlretrieve(url, path+os.path.split(url)[1]) 