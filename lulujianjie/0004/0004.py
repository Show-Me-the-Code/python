import re
lines_count = 0
#words_count = 0
chars_count = 0
lines_list = []
words_list = {}
with open('./test.txt','r') as f:
#http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386820066616a77f826d876b46b9ac34cb5f34374f7a000
    for line in f:## 使用文件迭代器 , 每次只读取和显示一行
#http://blog.csdn.net/mvpme82/article/details/5674200
         lines_count += 1
         chars_count += len(line)#算空格
#正则表达式http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386832260566c26442c671fa489ebc6fe85badda25cd000
         lines_list = re.findall(r'[a-zA-Z\-]+',line)
         print lines_list
         for i in lines_list:
              #words_count += 1
              if i not in words_list:
                   words_list[i] = 1
              else:
                   words_list[i] += 1

    print 'lines_count:',lines_count
    print 'chars_count:',chars_count
    print 'words_count:',len(words_list)#输出字典的元素个数

for word,quantity in words_list.items():
     print word,'\'s number is ',quantity
      ##  f.close()
