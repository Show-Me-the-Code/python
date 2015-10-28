#!/usr/bin/env python
#coding: utf-8
import cmd
import sys

# 存放敏感词文件的路径
filtered_words_filepath = '/home/bill/Desktop/filtered_words.txt'

class CLI(cmd.Cmd):

    def __init__(self):
        # 初始化，提取敏感词列表
        cmd.Cmd.__init__(self)
        self.intro = 'Filtered Words Detective'
        self.words = map(lambda i: i.strip('\n'), open(filtered_words_filepath).readlines())
        self.prompt = "> "    # define command prompt

    def default(self, line):
        if any([i in line for i in self.words]):
            print 'Freedom'
        else:
            print 'Human Rights'

    def do_quit(self, arg):
        exit()
        return True

if __name__ =="__main__":
    cli = CLI()
    cli.cmdloop()