# -*- coding:utf-8 -*-
from lxml import etree
from bs4 import BeautifulSoup
#本想用lxml解析，不知为何打不开此html文件，上网查不到原因，换了本不想用的美汤。
soup = BeautifulSoup(open('AGitPro.html'),'lxml')
for section in soup.article.stripped_strings:
    print section
