"""
第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，
为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券
"""
import random
import string

def gene_activation_code(number,length):
    #numer 激活码的个数，length 激活码的长度
    resultlist = []
    #激活码由数字和字母组成
    source = string.ascii_letters + string.digits

    while len(resultlist) < number:
        actcode = ''
        for index in range(length):
            actcode += random.choice(source)
        if actcode in resultlist:
            pass
        else:
            resultlist.append(actcode)

    for actcode in resultlist:
        print(actcode)



if __name__ == "__main__":
#生成200个长度为10的由数字和字母组合的不重复激活码
    gene_activation_code(200,10)
