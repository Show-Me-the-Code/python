from urllib import urlopen
from bs4 import BeautifulSoup

f = urlopen('http://tieba.baidu.com/p/2166231880').read()
#print f
s = BeautifulSoup(f)
s_imgs = s.find_all('img', pic_type='0')
#print s_img
i=1
for s_img in s_imgs:
    img_url = s_img['src']
    img_content = urlopen(img_url).read()
    print img_url
    file_name = str(i) + '.jpg'
    with open(file_name, 'wb') as wf:
        wf.write(img_content)
    i += 1
    
    
