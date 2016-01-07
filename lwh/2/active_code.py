"""
做为 Apple Store App 独立开发者，你要搞限时促销，
为你的应用生成激活码（或者优惠券），
使用 Python 如何生成 200 个激活码（或者优惠券）？

激活码格式:
19个字符组成,分成4组,中间用"-"连接起来
必须同时包含大小写字母数字

"""
import random
import string


def generate_active_code():
    active_code = []
    ascii_ = string.ascii_letters + string.digits
    active_code = ["".join([random.choice(ascii_) for i in range(16)])
                   for i in range(200)]

    return active_code

if __name__ == "__main__":
    active_code = generate_active_code()
    print(active_code)
