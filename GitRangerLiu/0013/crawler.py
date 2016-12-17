
import urllib3 as ul
import urllib3
import certifi
import urllib3.contrib.pyopenssl as pyopenssl
from bs4 import BeautifulSoup as bs
import time

link = 'http://tieba.baidu.com/p/2166231880'

def crawler(link):
    html = get_html(link)
    (piclinks, filename) = get_pic_link(html)
    print piclinks
    #download
    i = 0
    for link in piclinks[:]:
        download(link, filename + str(i) + '.jpg')
        i += 1
        #time.sleep(10)

def get_html(link):
    pyopenssl.inject_into_urllib3()
    http = ul.PoolManager(cert_reqs = 'CERT_REQUIRED', \
                          ca_certs = certifi.where())
    r = http.request('GET', link)
    return r.data

def get_pic_link(html):
    soup = bs(html, 'html.parser')
    purls = [link.get('src') for link in soup.find_all('img')]
       
    #the title of the page as the picture fielname
    filename = soup.find('title').get_text()   
    return (purls, filename)


def download(url, filename):
    pyopenssl.inject_into_urllib3()
    http = ul.PoolManager(cert_reqs = 'CERT_REQUIRED', \
                          ca_certs = certifi.where())
    res = http.request('GET', url)
    with open(filename, 'wb') as f:
        f.write(res.data)
   
if __name__ == '__main__':
    crawler(link)
