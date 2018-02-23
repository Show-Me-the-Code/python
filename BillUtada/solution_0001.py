import string
import random

#config
number = 200;
couponLenth = 16;
out = './Sources/coupons';
field = string.digits + string.letters;

if __name__ == '__main__':

    with open(out, 'w') as f:
        for num in range(0, number):

            coupon = [];

            for index in range(couponLenth):
                coupon.append(str(random.choice(field)));

            f.write(''.join(coupon) + '\n')

    f.close();

    print 'successfully generate %s coupons' % str(number)
