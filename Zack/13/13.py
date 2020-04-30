# 用 Python 写一个爬图片的程序，爬 这个链接里的日本妹子图片 :-) https://tieba.baidu.com/p/2166231880?red_tag=0100525148

import requests
from bs4 import BeautifulSoup
import os

result_path = './imgs/'
if not os.path.isdir(result_path):
    os.mkdir(result_path)
    print('directory made')

url = 'https://tieba.baidu.com/p/2166231880?red_tag=0100525148'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'lxml')
ims = soup.find_all('img', {'class': 'BDE_Image'})
for im in ims:
    img_name = os.path.split(im['src'])[1]
    with open(os.path.join(result_path, img_name), 'wb') as f:
        f.write(requests.get(im['src']).content)
        print(requests.get(im['src']).content)
