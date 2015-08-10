# 爬图片
import requests

from PIL import Image
from bs4 import BeautifulSoup
from io import BytesIO
import os


def fetch_imgs(url, save_dir, exts=None):
    print('- start running...')
    resp = BeautifulSoup(requests.get(url).text, 'lxml')
    img_list = resp.find_all('img')
    for i, img_url in enumerate(img_list):
        ext = os.path.splitext(img_url['src'])[-1]
        if exts and ext not in exts:
            continue
        fn = '{i}{ext}'.format(i=i, ext=ext)
        print('- saving {fn}'.format(fn=fn))
        try:
            img_str = requests.get(img_url['src'], timeout=5).content
        except Exception as e:
            print(e)
            continue
        img = Image.open(BytesIO(img_str))
        img.save(save_dir + fn)


if __name__ == '__main__':
    url = 'http://tieba.baidu.com/p/2166231880'
    save_dir = '.'
    fetch_imgs(url, save_dir, ['.gif'])
