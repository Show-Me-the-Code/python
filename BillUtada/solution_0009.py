from bs4 import BeautifulSoup

#config
HTMLPATH = '/home/william/pythonPractice/Sources/cd.html'

if __name__ == '__main__':
    with open(HTMLPATH, "r") as f:
        page = BeautifulSoup(f, "lxml");
        urls = page.findAll('a');
        for url in urls:
            if "href=\"" in str(url) and url['href'] is not '':
                print url['href']
