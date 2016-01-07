# coding = 'utf-8'
__author__ = 'Forec'

import requests
from bs4 import BeautifulSoup
import re
import pdb

# url = input()
url = 'http://forec.github.io/2015/11/01/Computer-Organization-Architecture5/'
html = requests.get(url)

soup = BeautifulSoup(html.text,"html.parser")
print(soup.body.text.encode('GBK','ignore').decode('GBK'))