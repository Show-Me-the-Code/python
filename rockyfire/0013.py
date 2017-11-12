import requests
from bs4 import BeautifulSoup


# 获取链接
def crawler_image(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    sum = 0
    for x in soup.find_all("img", attrs={"class": "BDE_Image"}):
        # print (sum,'.jpg')
        down_load(x['src'], str(sum) + '.jpg')
        sum += 1


# 下载图片
def down_load(img_src, img_name):
    res = requests.get(img_src)
    with open(img_name, 'wb') as f:
        f.write(res.content)


crawler_image("http://tieba.baidu.com/p/2166231880")
