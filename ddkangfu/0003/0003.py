#coding=utf-8

import uuid

import redis

"""
003, 将 0001 题生成的 200 个激活码（或者优惠券）保存到 **Redis** 非关系型数据库中.
"""


def get_redis_instance(host='localhost', port=6379):
    return redis.StrictRedis(host=host, port=port)


def generate_activation_code(count):
    code_list = []
    for i in xrange(count):
        code = str(uuid.uuid4()).replace('-', '').upper()
        if not code in code_list:
            code_list.append(code)

    return code_list


def store_to_redise(codes):
    if codes:
        cache = get_redis_instance()

        try:
            cache.set('code:count', len(codes))
            
            for i in xrange(len(codes)):
                cache.set('code:{0}'.format(i), codes[i])

            cache.save()
            return True
        except:
            print 'Can not connect to redis server !!!'

    return False


def print_activation_code():
    cache = get_redis_instance()

    try:
        count = cache.get('code:count')

        count = 0 if count is None else int(count) 
        
        for i in xrange(count):
            print cache.get('code:%d'%i)
    except:
        print 'Can not connect to redis server !!!'


if __name__ == "__main__":
    code_list = generate_activation_code(200)
    if store_to_redise(code_list):
        print_activation_code()
