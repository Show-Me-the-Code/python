#coding:utf-8
import requests, re, os

url = 'http://tieba.baidu.com/p/2166231880'

header = {
        'Accept': '*/*',
        'Accept-Encoding':'gzip,deflate,sdch',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Connection':'keep-alive'
        }
html = requests.get(url,headers = header)

data = html.content.decode('utf-8')
find = re.compile(r'<img pic_type="0" class="BDE_Image" src="(.*?).jpg" bdwater')
result = find.findall(data)

for img_url in result:
    name = img_url.split('/')[-1]
    img_url = img_url+'.jpg'
    html = requests.get(img_url,headers = header)
    im = html.content
    with open(name+'.jpg','wb')as f:
        f.write(im)
