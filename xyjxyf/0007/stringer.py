# coding = utf-8

import random, string

/*
sdfhjdsf
hgjh
*/
# def Unicode():
#     val = random.randint(0x4E00, 0x9FBF)
#     return unichr(val)
#
# # 随机汉字
# def GB2312():
#     head = random.randint(0xB0, 0xCF)
#     body = random.randint(0xA, 0xF)
#     tail = random.randint(0, 0xF)
#     val = ( head << 8 ) | (body << 4) | tail
#     str = "%x" % val
#     return str.decode('hex').decode('gb2312')

# 随机字母
def rand_char():
    return chr(random.randint(65, 90))

# 随机字母或者数字
def rand_choice():
    str = 'abcdefghigklmnopqrstuvwxyzQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
    return random.choice(str)
