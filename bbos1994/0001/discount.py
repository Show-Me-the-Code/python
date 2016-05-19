#! /usr/bin/python3
# -*-coding:utf-8 -*-

__author__ = 'TonyZhu'

from random import randint

str = 'abcdefghigklmnopqrstuvwxyz123456789'

def produce(count):
	discountNumArray = []
	for _count in range(count):
		discountNum = []
		for i in range(10):
			_index = randint(0,34)
			discountNum.append(str[_index])
		discountNumArray.append(''.join(discountNum))
	return discountNumArray



if __name__  == '__main__':
	discountNumArray = produce(10)
	for _array in discountNumArray:
		print(_array)