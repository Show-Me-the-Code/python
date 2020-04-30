# 第 0009 题： 一个HTML文件，找出里面的链接。

from bs4 import BeautifulSoup
import requests

url = 'https://github.com/A1014280203/show-me-the-code'
resp = requests.get(url)
soup = BeautifulSoup(resp.text,'lxml')
url_link = soup.find_all('a')
for url in url_link:
    print(url['href'])

