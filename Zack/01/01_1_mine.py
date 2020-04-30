# 第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
from random import randint

string = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
# print(len(string))
# print(randint(0,63))

def get_code(digit):
    code = ''
    for i in range(digit):
        code += string[randint(0,61)]
    return code

def save_code():
    with open('coupon1.txt', 'w') as f:
        for i in range(200):
            code = get_code(10)
            f.write(code+'\n')

if __name__ == '__main__':
    save_code()