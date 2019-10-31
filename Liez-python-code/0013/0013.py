# 网址：http://tieba.baidu.com/p/4341640851

import os
import re
import urllib.request

def pic_collector(url):
    content = urllib.request.urlopen(url).read()
    r = re.compile('<img class="BDE_Image" pic_type="1" width="450" height="450" src="(.*?)" ')
    pic_list = r.findall(content.decode('utf-8'))

    os.mkdir('pic_collection')
    os.chdir(os.path.join(os.getcwd(), 'pic_collection'))
    for i in range(len(pic_list)):
        pic_num = str(i) + '.jpg'
        urllib.request.urlretrieve(pic_list[i], pic_num)
        print("success!" + pic_list[i])

pic_collector("http://tieba.baidu.com/p/4341640851")
