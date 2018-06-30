# -*- coding:utf-8 -*-
import os, collections

'''practice5中遍历目录中文件的方法，读取所有文件'''
diarydir = r'./diary/'
file_list = os.walk(diarydir)
s = set()
map = {}

