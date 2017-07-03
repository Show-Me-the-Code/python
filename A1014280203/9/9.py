import requests
import pyquery

url = 'https://github.com/A1014280203/show-me-the-code'
url_list = list()
resp = requests.get(url)
doc = pyquery.PyQuery(resp.content.decode())
a_tags = doc.find('a')
for a in a_tags.items():
    if a.attr('href').startswith('http'):
        url_list.append(a.attr('href'))
    elif a.attr('href').startswith('/'):
        url_list.append('https://github.com' + a.attr('href'))
print(url_list)