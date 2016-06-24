# coding = utf-8
__author__ = 'forec'
import random

def make_number( num, length ):
    str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    b = set()
    i = 0
    while i < num:
        ans = ''
        for j in range(length):
            ans += random.choice(str)
        if ans not in b:
            b |= {ans}
            i += 1
            print(ans)

make_number( 200, 10)