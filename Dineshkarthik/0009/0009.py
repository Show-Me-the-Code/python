#!/usr/local/bin/python
#coding=utf-8
__author__ = 'Dineshkarthik'

#0008 Title: an HTML file, find the inside of the link .


import urllib2
from bs4 import BeautifulSoup

url = "https://www.google.com"
page = urllib2.urlopen(url)

soup = BeautifulSoup(page)
links = soup.findAll('a')
for link in links:
    print(link['href'])