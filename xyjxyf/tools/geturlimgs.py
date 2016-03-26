# encoding = utf-8

import socket, os
from urllib import request
from bs4 import BeautifulSoup

class geturlimgs(object):

    def __index__(self, to_dir=None):
        self.to_dir = None

    # 伪装浏览器,以免被封
    def user_agent(self, url):
        req_header = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
        req_timeout = 20
        try:
            req = request.Request(url,None,req_header)
            html = request.urlopen(req,None,req_timeout)
        except request.URLError as e:
            print(e.message)
        except socket.timeout as e:
            # user_agent(url)
            print("timeout")

        return html

    def get_img_links(self, url=None):
        if url is None or len(url) == 0:
            return None
        html = self.user_agent(url)
        soup = BeautifulSoup(html, "lxml")

        count = 0
        links = []
        items = soup.find_all('img')
        for item in items:
            link = item.get('src')
            links.append(link)

        return links

    def download_imgs(self, links, to_dir):
        if links is None or len(links) == 0:
            return

        if not os.path.exists(to_dir):
            os.makedirs(to_dir)

        if not to_dir.endswith('/'):
            to_dir = to_dir + '/'

        index = 0
        for url in links:
            end = os.path.splitext(url)[1]
            if len(end) == 0:
                end = ".jpg"
            img_path = to_dir + '%i%s' % (index, end)
            image = request.urlretrieve(url, img_path)
            index = index + 1

    def get_imgs(self, url=None, to_dir=None):
        if url is None or to_dir is None:
            return None

        links = self.get_img_links(url)
        return self.download_imgs(links, to_dir)
