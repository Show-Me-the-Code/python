#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-13
# Blog: morningchen.com

import os


def creat_file(path):
    """
        在指定目录创建子文件夹 0000～0025
    """
    for i in range(26):
        n = str(i).zfill(4)
        sub_path = path + n
        os.mkdir(sub_path)
    return path

if __name__ == '__main__':
    path = "/Users/chan/python/chen2aaron/"
    creat_file(path)
