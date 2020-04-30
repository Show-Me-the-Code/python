# 第 0008 题： 一个HTML文件，找出里面的正文。

from bs4 import BeautifulSoup
with open('local-ntp.html') as f:
    soup = BeautifulSoup(f, 'lxml')
    print(soup.body.text.strip('\n'))