#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Date: 23-02-15
# Author: Liang

import random
import string

coupon_number = 200
coupon_size = 12

for i in range(coupon_number):
    coupon = ''.join(
        random.sample(string.digits + string.ascii_uppercase, coupon_size))
    print(coupon)
