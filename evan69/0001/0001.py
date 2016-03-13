# -*- coding: utf-8 -*-
# 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？

import uuid

def produce_str(num = 200):
	str_list = []
	i = 0
	while True:
		i = i + 1
		if i > num:
			break
		mystr = str(uuid.uuid1()).replace('-','')
		if mystr not in str_list:
			str_list.append(mystr)
	return str_list


a = produce_str()
print a
