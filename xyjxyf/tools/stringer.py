# coding = utf-8

import random, string

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

# 将字典转为json格式
def dict_to_json(object=None, begin_indent="", indent=u'\t', newl=u'\n'):
    if object is None:
        return None

    if type(object) is not dict:
        return None

    ret_str = u'{' + newl
    space = begin_indent + indent
    for key in object:
        ret_str = ret_str + space + key + ": "
        item = object[key]
        ret_str = ret_str + u'%s,' % str(item)
        # if type(item) is list:
        #     list_to_json(item)
        # elif type(item) is dict:
        #     dict_to_json(item)
        # else:
        #     str
        ret_str = ret_str + begin_indent + newl

    ret_str = ret_str + begin_indent + u'}'

    return ret_str


# 将数组转为json格式
def list_to_json(object=None, begin_indent="", indent=u'\t', newl=u'\n'):
    if object is None:
        return None

    if type(object) is not list:
        return None

    ret_str = u'[' + newl
    space = begin_indent + indent
    for item in object:
        ret_str = ret_str + space + u'%s,' % str(item)
        # if type(item) is list:
        #     list_to_json(item)
        # elif type(item) is dict:
        #     dict_to_json(item)
        # else:
        #     str
        ret_str = ret_str + begin_indent + newl

    ret_str = ret_str + begin_indent + u']'

    return ret_str