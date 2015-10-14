#!usr/bin/python
#coding=utf-8

"""
第 0006 题：你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，
假设内容都是英文，请统计出你认为每篇日记最重要的词。
"""

import os


def walk_dir(path):
	for root, dirs, files in os.walk(path):
		for f in files:
			if f.lower().endswith('txt'):
				