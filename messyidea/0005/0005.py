#!/usr/bin/env python
# coding=utf-8

from PIL import Image

org = Image.open('./origin.jpg')
org = org.resize((50,50), Image.ANTIALIAS)
org.save('rst', 'jpeg')
