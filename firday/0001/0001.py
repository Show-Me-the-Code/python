__author__ = 'friday'
import random
def randomnum(num=20,long=10):
    str = 'qwertyuiopasdfghjklzxcvbnm_^@1234567890*&%$#!~'
    b = []
    for j in range(num):
        a = ''
        for i in range(long):
            a += random.choice(str)
        b.append(a)
    i = 0
    while i < (len(b)-4):
        print(b[i:i+5])
        i +=5

if __name__ == '__main__': randomnum()