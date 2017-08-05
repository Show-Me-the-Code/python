# coding:utf-8

from lxml import etree

def getxpath(html):
    return etree.HTML(html)    


# sample1 = """<html>
#   <head>
#     <title>My page</title>
#   </head>
#   <body>
#     <h2>Welcome to my <a href="#" src="x">page</a></h2>
#     <p>This is the first paragraph.</p>
#     <!-- this is the end -->
#   </body>
# </html>
# """

# sample2 = """
# <html>
#   <body>
#     <ul>
#       <li>Quote 1</li>
#       <li>Quote 2 with <a href="...">link</a></li>
#       <li>Quote 3 with <a href="...">another link</a></li>
#       <li><h2>Quote 4 title</h2> ...</li>
#     </ul>
#   </body>
# </html>
# """

# sample3 = """<html>
#   <body>
#     <ul>
#       <li id="begin"><a href="https://scrapy.org">Scrapy</a>begin</li>
#       <li><a href="https://scrapinghub.com">Scrapinghub</a></li>
#       <li><a href="https://blog.scrapinghub.com">Scrapinghub Blog</a></li>
#       <li id="end"><a href="http://quotes.toscrape.com">Quotes To Scrape</a>end</li>
#       <li data-xxxx="end" abc="abc"><a href="http://quotes.toscrape.com">Quotes To Scrape</a>end</li>
#     </ul>
#   </body>
# </html>
# """
# s3 = getxpath(sample3)

sample4 = u"""
<html>
  <head>
    <title>My page</title>
  </head>
  <body>
    <h2>Welcome to my <a href="#" src="x">page</a></h2>
    <p>This is the first paragraph.</p>
    <p class="test">
    编程语言<a href="#">python</a>
    <img src="#" alt="test"/>javascript
    <a href="#"><strong>C#</strong>JAVA</a>
    </p>
    <p class="content-a">a</p>
    <p class="content-b">b</p>
    <p class="content-c">c</p>
    <p class="content-d">d</p>
    <p class="econtent-e">e</p>
    <p class="heh">f</p>
    <!-- this is the end -->
  </body>
</html>
"""
s4 = etree.HTML(sample4)


# get lxml construction
# s2 = getxpath(sample2)    
# print(s2.xpath('//li/text()'))



# print(s1.xpath('//title/text()'))
# print(s1.xpath('/html/head/title/text()'))

# print(s1.xpath('//h2/a/@href'))

# print(s1.xpath('//text()'))

# print(s1.xpath('//comment()'))