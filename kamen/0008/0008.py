from bs4 import BeautifulSoup
from urllib import urlopen

r = urlopen('http://sports.sina.com.cn/nba/2015-04-23/00007584374.shtml').read()
soup = BeautifulSoup(r)
#print soup
t = soup.find_all(id='artibody')
#print t
#print type(t)
s=''
for p in t[0].find_all("p"):
    s = s + p.get_text()+'\n'

print s



