# Source:https://github.com/Show-Me-the-Code/show-me-the-code
# Author:renzongxian
# Date:2014-12-19
# Python 3.4

"""

第 0009 题：一个HTML文件，找出里面的链接。

"""

import urllib.request
import re


def find_links(website):
    html_content = urllib.request.urlopen(website).read()
    r = re.compile('href="(.*?)"')
    result = r.findall(html_content.decode('GBK'))
    return result

if __name__ == '__main__':
    print(find_links('http://www.taobao.com/'))