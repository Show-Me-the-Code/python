from bs4 import BeautifulSoup
from urllib import urlopen
r = urlopen('http://sports.sina.com.cn/nba/2015-04-23/00007584374.shtml').read()
soup = BeautifulSoup(r)

#there is javasciript things to be cleaned.
s = soup.find_all("a")
for link in s:
    try:
        print link["href"]
    except KeyError:
        pass

