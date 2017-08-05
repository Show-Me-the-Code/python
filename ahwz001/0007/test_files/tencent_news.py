#coding:utf-8

import requests
from bs4 import BeautifulSoup

url = 'http://news.qq.com/'

wbdata = requests.get(url).content

soup = BeautifulSoup(wbdata,'lxml')

news_titles = soup.select('div.text > em.f14 > a.linkto')

for n in news_titles:
    title = n.get_text()
    link = n.get('href')
    # data = {'title':title,
    #                 'link':link}
    print title,
    print link

