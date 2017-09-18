# -*- coding:utf-8 -*-

'''

第 0008 题：一个HTML文件，找出里面的正文。

@Author monkey
@Date   2017-8-31
'''
import json

from bs4 import BeautifulSoup


def findContent():
    path = "The world's leading software development platform · GitHub.html"

    with open(path, encoding='UTF-8') as file:
        soup = BeautifulSoup(file)

    # print(soup.prettify())
    print(soup.body)



if __name__ == '__main__':
    findContent()