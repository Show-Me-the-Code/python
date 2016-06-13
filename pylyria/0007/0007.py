#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#  Copyright By PyLyria
# CreateTime: 2016-03-04 19:36:40
import os

def get_path(root = os.curdir):
    root += os.sep
    for path, dirs, files in os.walk(root):
        for file_name in files:
            yield path, file_name

def get_lines(file_name):
    with open(file_name,'rt',encoding='utf-8') as f:
        for line in f:
            yield line.strip()

if __name__ == '__main__':
    paths = get_path()
    format = ('.py', '.c', '.cpp', '.sql')
    annotation = ('#', '//', '--', '/*')
    code_statistics = {}

    for path, file_name in paths:
        if file_name.endswith(format):
            code_statistics[file_name] = {}
            lines = get_lines(path + os.sep + file_name)
            for line in lines:
                if len(line) ==0:
                    code_statistics[file_name]['EmptyLine'] = code_statistics[file_name].get('EmptyLine', 0) + 1
                elif line.startswith(annotation):
                    code_statistics[file_name]['AnnotationLine'] = code_statistics[file_name].get('AnnotationLine', 0) + 1
                else:
                    code_statistics[file_name]['CodeLine'] = code_statistics[file_name].get('CodeLine', 0) + 1

    print(code_statistics)
