import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import re
def getHref(link):
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	headers = { 'User-Agent' : user_agent }
	request = urllib.request.Request(url=link,headers=headers)
	response = urllib.request.urlopen(request)
	htmlCont = response.read().decode('UTF-8')
	soup = BeautifulSoup(htmlCont,'html.parser')
	for link in soup.findAll('a'):
		print(link['href'])

getHref('http://blog.csdn.net/zsuguangh/article/details/6226385')