"""
第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，
为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券
"""
import string, random

#激活码中的字符和数字
field = string.ascii_letters + string.digits

#获得四个字母和数字的随机组合
def get4Random():
    return "".join(random.sample(field,4))

#生成的每个激活码中有几组
def concatenate(group):
    return "-".join([get4Random() for i in range(group)])

#生成n组激活码
def generate(n):
    return [concatenate(4) for i in range(n)]

if __name__ == '__main__':
    print(generate(200))
