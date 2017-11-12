0008&0009

import codecs
from lxml import etree

f = codecs.open("/pythontext/PythonNotes/test/test.html", "r", "utf-8")
content = f.read()
f.close()

tree = etree.HTML(content)
for p in tree.xpath("//p/text()"):
    if p == "":
        continue
    print(p)

for a in tree.xpath("//a/@href"):
    if a == "":
        continue
    print(a)

# BeautifulSoup
from bs4 import BeautifulSoup

soup = BeautifulSoup(content, 'html.parser')

for p in soup.find_all("p"):
    print(p.string)

for a in soup.find_all("a"):
    if a['href'] != "":
        print(a['href'])
