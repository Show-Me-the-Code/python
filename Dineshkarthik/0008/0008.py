#!/usr/local/bin/python
#coding=utf-8
__author__ = 'Dineshkarthik'

#0008 Title: an HTML file, find the inside of the body .


import urllib2
from bs4 import BeautifulSoup

url = "https://www.google.co.in"
page = urllib2.urlopen(url)

soup = BeautifulSoup(page)
print soup.body.text