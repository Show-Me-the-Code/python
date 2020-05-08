# -*- coding: utf-8 -*-
"""
Created on Fri May  8 10:08:30 2020

@author: saurabh
"""

import subprocess
def PingIP(str):
    process=subprocess.Popen(str,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    for line in process.stdout:
        print(line)
    res.append(line)
    errcode = process.returncode
    for line in res:
        print(line)
res=[]
file1=open("groupofIPs.txt","r+")
grp=file1.read().split('\n')
cmd='ping'

for item in grp:
    cmd1=cmd +" "+item
    PingIP(cmd1)
