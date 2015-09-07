# coding=utf-8
__author__ = 'PyBeaner'
from bs4 import BeautifulSoup


def get_links(html):
    soup = BeautifulSoup(html)
    links = []
    for link in soup.find_all("a"):
        href = link["href"]
        if href.startswith("http"):
            links.append(href)
    return links


if __name__ == '__main__':
    import requests

    r = requests.get("https://github.com/")
    html = r.text
    links = get_links(html)
    print(links)
