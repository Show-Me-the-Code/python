# coding:utf-8
# qiushibaike.py


import requests
from bs4 import BeautifulSoup
import time
import random
import os


def make_url(num = 10):    
    res = []
    url_base = 'http://www.qiushibaike.com/8hr/page/num/?s=4970693'
    url_base = 'http://www.qiushibaike.com/hot/page/num/'
    for i in range(1,num+1):
        t = url_base.replace('num',str(i))
        res.append(t)
    # for i in res:
    #     print i
    return res


def deal_request(url):
    header = {
    'Referer':'http://www.qiushibaike.com/',
    'User-Agent':
    'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36'}
    r = requests.get(url, headers=header)
    print url
    return r.content


def parse_html(html):
    res = []
    soup = BeautifulSoup(html,'lxml')
    content = soup.find_all('div',attrs={'class':'content'})
    for i in content:
        # print i
        t = i.get_text()
        res.append(t)
    return res


def save_result(li):
    fn = open('qiushibaike_hot.txt','a')
    for i in li:
        t = i.encode('utf-8')
        fn.write(t)
    fn.write('\n\n\n')
    fn.close()
    print 'well done!'


def main():
    url = make_url()
    for i in url:
        j = random.randint(3,7)
        time.sleep(j)  
        t = deal_request(i)
        p = parse_html(t)
        save_result(p)
        

if __name__ == '__main__':
    main()
    os.system('cat qiushibaike_hot.txt |more')