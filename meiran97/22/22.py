# 第 0022 题： iPhone 6、iPhone 6 Plus 早已上市开卖。请查看你写得 第 0005 题的代码是否可以复用。
# 学习了如何调用不同文件夹内的py
import sys

sys.path.append(r'/Users/meizhenhai/PycharmProjects/python_everyday/05/')
'''python import模块时， 是在sys.path里按顺序查找的。
sys.path是一个列表，里面以字符串的形式存储了许多路径。
使用A.py文件中的函数需要先将他的文件路径放到sys.path中'''
import nice_one

if __name__ == '__main__':
    nice_one.zoom(1134, 750)
