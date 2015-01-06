import string
import random

"""
generate COUPON_NUM coupons,every coupon consists of
COUPON_STR_LEN digit which are capital letter or 0~9 
"""
COUPON_NUM = 200
COUPON_STR_LENGTH = 8

if __name__ == "__main__":
	lst = list(string.letters)[26:] + list(string.digits)
	for i in range(COUPON_NUM):
		coupon_list = [random.choice(lst) for i in range(COUPON_STR_LENGTH)]
		coupon_str = "".join(coupon_list)
		print coupon_str

			
		
	
