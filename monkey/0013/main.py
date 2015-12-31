# -*- coding:utf-8 -*-
from lxml import etree
import requests
import urllib

__author__ = 'monkey'


# 获取url地址，对页面进行爬去
def spider(url):
    html = requests.get(url)
    selector = etree.HTML(html.text)

    picitems = []
    picitems = selector.xpath('//div[@class="d_post_content j_d_post_content  clearfix"]/img[@class="BDE_Image"]')
    print(len(picitems))

    i = 0
    for pic in picitems:
        url = pic.xpath('@src')[0]
        #print(url)
        dir = './%d.jpg'%i
        download_Image(url, dir)
        i += 1


# 下载图片
def download_Image(url, save_path):
    urllib.request.urlretrieve(url, save_path)


if __name__ == '__main__':
    url = "http://tieba.baidu.com/p/2166231880"
    spider(url)