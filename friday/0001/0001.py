__author__ = 'friday'
import random

def creat_num(num,long):
    str = 'qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*_+'
    b = []
    for i in range(num):
        a = ''
        for j in range(long):
            a += random.choice(str)
        b.append(a)
    for i in range(len(b)):
        print(b[i])

if __name__ == '__main__':
    creat_num(200,10)