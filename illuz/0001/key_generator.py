#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author:      illuz <iilluzen[at]gmail.com>
# File:        key_generator.py
# Create Date: 2015-02-09 10:43:36
# Descripton:  Use uuid module to generate 200 register keys.
# Usage:       key_generator.py

"""
第 0001 题：
做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
"""

from uuid import uuid4

def generate_key(num):
    key_list = [str(uuid4()) for i in range(num)]
    return key_list


def main():
    print generate_key(200)


if __name__ == '__main__':
    main()

