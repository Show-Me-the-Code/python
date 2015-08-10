# 获取页面链接
import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':
    url = 'https://www.83chedai.com'
    resp = BeautifulSoup(requests.get(url).text, 'lxml')
    a_list = resp.find_all('a')
    for a in a_list:
        print(a['href'], ' : ', a.get_text().strip())
