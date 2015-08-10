# 获取web页面的内容
import re
import requests

from bs4 import BeautifulSoup


def get_string(data):
    ret = []
    for child in data.children:
        if child != child.string:
            r = get_string(child)
            if r:
                ret.append(r)
                return '\n'.join(ret)
        else:
            return child

if __name__ == '__main__':
    url = 'http://jproxy.io/account/home/'
    resp = BeautifulSoup(requests.get(url).text, 'lxml')
    # 只搜索 p h* title 元素
    re_obj = re.compile(r'^(p|h(\d)|title)$')
    content = resp.find_all(re_obj)
    s = []
    for item in content:
        r = get_string(item)
        if r:
            s.append(r)
    s = '\n'.join(s)
    print(s)
