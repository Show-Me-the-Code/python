#coding = utf-8
# 输入链接
__author__ = 'Forec'

import requests
import re
from bs4 import BeautifulSoup

url = input()
html = requests.get(url)

soup = BeautifulSoup(html.text,"html.parser")
find_href = soup.findAll('a')
for x in find_href:
    print(x['href'])