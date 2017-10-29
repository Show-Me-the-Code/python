# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup

soup = BeautifulSoup(open('AGitPro.html'),'lxml')
for link in soup.find_all('a'):
    print link['href']