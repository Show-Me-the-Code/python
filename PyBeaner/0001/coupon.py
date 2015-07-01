__author__ = 'PyBeaner'
from random import choice
import string

chars = string.ascii_uppercase + string.digits


def generate_coupons(count, coupon_length=5):
    coupons = []
    for i in range(count):
        coupon = generate_one_coupon(coupon_length=coupon_length)
        while coupon in coupons:
            coupon = generate_one_coupon(coupon_length)

        coupons.append(coupon)

    return coupons


def generate_one_coupon(coupon_length=5):
    coupon = []
    for i in range(coupon_length):
        ch = choice(chars)
        coupon.append(ch)
    return "".join(coupon)


if __name__ == '__main__':
    coupons = generate_coupons(200, 5)
    print(coupons)
