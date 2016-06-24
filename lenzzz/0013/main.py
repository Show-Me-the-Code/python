# python3
#coding:utf-8
import requests
from bs4 import BeautifulSoup

def downloadPic(url):
    req = requests.get(url)
    imageName = url.split('/')[-1]
    with open(imageName, 'wb') as fp:
        fp.write(req.content)

html = requests.get("http://tieba.baidu.com/p/2166231880").content
soup = BeautifulSoup(html, "html.parser")
for img in soup.find_all("img", {"class", "BDE_Image"}):
    downloadPic(img['src'])

