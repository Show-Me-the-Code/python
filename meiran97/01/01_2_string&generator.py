import string
import random

char = list(string.ascii_letters)+list(string.digits)
# print(type(char))

def gen_coupon(digit, num):
    with open('coupon.txt', 'w') as fh:
        for i in range(num):
            lst = [random.choice(char) for i in range(digit)]
            coupon = "".join(lst)+'\n'
            fh.write(coupon)

if __name__ == '__main__':
    gen_coupon(8, 200)

