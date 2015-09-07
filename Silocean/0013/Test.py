__author__ = 'Tracy'
from urllib import urlopen
from bs4 import BeautifulSoup

f = urlopen('http://tieba.baidu.com/p/2166231880').read()

s = BeautifulSoup(f)

images = s.find_all('img', pic_type='0')
count = 1
def download(src):
    global count
    file_name = str(count) + '.jpg'
    content = urlopen(src).read()
    with open(file_name, 'wb') as f:
        f.write(content)
    count += 1

for image in images:
    download(image['src'])

