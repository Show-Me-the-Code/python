#-*-coding:utf-8-*-
import os
import re

def word_statistics(filePath):
    wordDict = {}
    with open(filePath,'rt') as f:
        for line in f:
            words = re.split('[,.\s]\s*',line)
            for word in words:
                if word.lower() in wordDict and word.isalpha():
                    wordDict[word.lower()] += 1
                elif word.lower() not in wordDict and word.isalpha():
                    wordDict[word.lower()] = 1
    
    wordSorted = sorted(zip(wordDict.keys(),wordDict.values()))

    for word,count in wordSorted:
        print(word,':',count)

if __name__ == '__main__':
    word_statistics(r'...\test.txt')

#output:
# a : 11
# about : 1
# access : 1
# algorithm : 1
# allowing : 3
# allowingwith : 1
# alone : 4
# an : 2
# and : 1
# anything : 1
# are : 1
# as : 3
# attribute : 1
# attributes : 6
# calling : 1
# calls : 1
# can : 6
# case : 1
# change : 1
# class : 4
# code : 5
# complicated : 4
# control : 1
# creates : 1
# defining : 1
# definition : 1
# do : 4
# drive : 1
# easily : 1
# easy : 5
# etc : 1
# everything : 4
# expose : 1
# extra : 2
# fact : 1
# fall : 4
# for : 6
# forget : 1
# function : 6
# functions : 4
# generator : 8
# generators : 4
# going : 1
# history : 1
# how : 1
# however : 1
# if : 7
# implement : 1
# in : 6
# instance : 1
# interact : 5
# internal : 1
# into : 4
# is : 6
# it : 9
# iteration : 1
# just : 1
# lead : 4
# like : 1
# loop : 1
# makes : 1
# method : 5
# methods : 1
# might : 1
# needs : 4
# normal : 1
# of : 10
# one : 1
# or : 1
# other : 5
# part : 1
# parts : 4
# potential : 1
# program : 4
# provide : 1
# putting : 1
# rather : 4
# require : 1
# shown : 2
# since : 1
# solution : 1
# state : 1
# step : 1
# subtlety : 1
# such : 1
# technique : 1
# than : 1
# that : 3
# the : 13
# this : 6
# to : 22
# trap : 4
# treat : 1
# trying : 4
# unusual : 4
# use : 2
# user : 1
# users : 1
# using : 1
# via : 1
# want : 1
# ways : 4
# with : 13
# would : 1
# write : 1
# you : 7
# your : 6
