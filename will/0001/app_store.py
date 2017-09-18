# 第 0001 题： 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
'''
想法思路：
    1. 字符串方式
    2. 时间戳方式
    3. UUID全局标识符,使用uuid1或者uuid5算法
    4. 加密算法
'''

import random, string, time, math, uuid

chars = string.ascii_letters + string.digits

def gen1():
    '''
    根据26个大小写字母和数字随机选择10个
    涉及模块：
        1. random:
            random.random()函数是这个模块中最常用的方法了，它会生成一个随机的浮点数，范围是在0.0~1.0之间。
            random.uniform()正好弥补了上面函数的不足，它可以设定浮点数的范围，一个是上限，一个是下限。
            random.randint()随机生一个整数int类型，可以指定这个整数的范围，同样有上限和下限值。
            random.choice()可以从任何序列，比如list列表中，选取一个随机的元素返回，可以用于字符串、列表、元组等。
            random.shuffle()如果你想将一个序列中的元素，随机打乱的话可以用这个函数方法。
            random.sample()可以从指定的序列中，随机的截取指定长度的片断，不作原地修改。
        2. string
            string.digits: 0-9
            string.printable：可打印字符集
            string.ascii_letters: 大小字母集
    '''
    key = ''.join(random.sample(chars, 10))
    #key2 = ''.join(random.choice(chars) for i in range(10))
    return key

def gen2():
    '''
    当前时间戳生成
        1. math.modf(x)返回一个list，包括小数部分及整数部分
        2. https://gist.github.com/willhunger/85b119793f01211de50db0e0a257dbf0
        3. http://www.wklken.me/posts/2015/03/03/python-base-datetime.html
    '''
    key = math.modf(time.time())[0]
    return key

def gen3():
    '''
    UUID:通用唯一识别码,由一组32位数的16进制数字所构成
        uuid1()——基于时间戳
            由MAC地址、当前时间戳、随机数生成。可以保证全球范围内的唯一性，但MAC的使用同时带来安全性问题，局域网中可以使用IP来代替MAC。
        uuid2()——基于分布式计算环境DCE（Python中没有这个函数）
            算法与uuid1相同，不同的是把时间戳的前4位置换为POSIX的UID，实际中很少用到该方法。
        uuid3()——基于名字的MD5散列值
            通过计算名字和命名空间的MD5散列值得到，保证了同一命名空间中不同名字的唯一性，和不同命名空间的唯一性，但同一命名空间的同一名字生成相同的uuid。
        uuid4()——基于随机数
            由伪随机数得到，有一定的重复概率，该概率可以计算出来。
        uuid5()——基于名字的SHA-1散列值
            算法与uuid3相同，不同的是使用 Secure Hash Algorithm 1 算法

    '''
    return uuid.uuid4()

for i in range(200):
    print(gen2())
