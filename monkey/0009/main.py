# -*- coding:utf-8 -*-

'''

第 0009 题：一个HTML文件，找出里面的链接。

@Author monkey
@Date   2017-8-31
'''
import json

from bs4 import BeautifulSoup


def findTagA():
    path = "The world's leading software development platform · GitHub.html"

    with open(path, encoding='UTF-8') as file:
        soup = BeautifulSoup(file)

    # print(soup.prettify())
    links = []
    for i in soup.find_all('a'):
        links.append(i['href'])

    print(links)

if __name__ == '__main__':
    findTagA()