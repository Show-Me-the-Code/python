#!/usr/bin/env python3
#get all pic in a url

from urllib.request import urlopen
from bs4 import BeautifulSoup

def img_crawler(url):
    content = url.read()
    bs_object = BeautifulSoup(content)
    bs_imgs = bs_object.find_all('img', pic_type='0')

    for img in bs_imgs:
        img_url = img['src']
        try:
            img_content = urlopen(img_url).read()
        except:
            pass
        print("Downloading... "+img_url)
        img_f = open(img_url.split('/')[-1], 'wb')
        img_f.write(img_content)
        img_f.close()
        print("Complete!")

if __name__ == '__main__':
    url = urlopen('http://tieba.baidu.com/p/2166231880')
    img_crawler(url)
