#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 30987
# @Date:   2015-01-12 17:03:52
# @Last Modified by:   30987
# @Last Modified time: 2015-01-12 17:21:29

#第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？


import uuid

def creat_code(number=10):
	result =[]

	while True is True:
		uuid_id=uuid.uuid1()
		tem = str(uuid_id).replace('-','')
		tmmmm=str(tem[4:])
		if not tmmmm in result:
			result.append(tmmmm)
		if len(result) is number:
			break
	print result

creat_code()