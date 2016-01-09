#-*- coding=utf-8
import xlwt
import xlrd
import re

book = xlrd.open_workbook(r'c:\python27\oneday_one\2015.xls')
print book.sheet_names()
sheet=book.sheet_by_index(0)
print sheet.name,sheet.nrows,sheet.ncols
col3=sheet.col_values(3)
li=[]
for i in col3:
    li.append(i)#.encode('utf-8')
del li[0]
s=[0,0]
info=re.compile(ur"(\d+)[\u4e00-\u9fa5](\d*)[\u4e00-\u9fa5]*")#匹配汉字！！！！
for each_time in li:
    t=info.match(each_time).groups()
    t=list(t)
    if u'' in t:
       t[1],t[0]=t[0],u'0'
    s[0]=s[0]+int(t[0])
    s[1]=s[1]+int(t[1])
s[0],s[1]=s[0]+int(s[1]/60),s[1]%60
print '通话时长累计%d分%d秒'%(s[0],s[1])

