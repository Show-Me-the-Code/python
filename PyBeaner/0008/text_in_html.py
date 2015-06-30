# coding=utf-8
__author__ = 'PyBeaner'
from bs4 import BeautifulSoup


def get_text(html):
    soup = BeautifulSoup(html)
    return soup.text


if __name__ == '__main__':
    import requests

    r = requests.get("https://github.com/")
    html = r.text
    text = get_text(html)
    with open("html.txt", "w+", errors="replace") as f:
        print(text, file=f)
        f.seek(0)
        for line in f:
            print(line)
