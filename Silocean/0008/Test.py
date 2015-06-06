
# -*- coding=utf-8 -*-

from bs4 import BeautifulSoup
import io
file = io.open('Test.html', 'r')
soup = BeautifulSoup(file)
print(soup.getText().strip("\n"))


file.close()
