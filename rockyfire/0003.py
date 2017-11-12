uuids=[]

import uuid

'''
uuid.uuid1()
uuid.uuid1
因为不加括号的结果是函数本身，
所以显示出来是一个 function；
加了括号以后是得到的结果是执行函数之后的返回值，
也就是计算出来的激活码。
显示中多出了 UUID()
是因为打印一个对象的时候会用对象里的 __repr__ 函数进行格式化后再输出，
而 __repr__ 一般会返回一个可以作为代码执行的字符串
（如果用 print 或者 str() 的话则是用 __str__ 函数格式化，
就没有 UUID() 了）
'''
for i in range(1,200):

    uuids.append(str(uuid.uuid4()))

print (uuids)

"""
    redis 命令
    安装                         sudo apt-get install redis-server  python3上使用 pip3 install redis
    查看是否启动(进入redis)        redis-cli
    查看配置                       config get *
    设置配置                        config set
    字符串                           set/get <name> hash-value
    Hash                             hmset/hgetall  <name> name
    List                               lpush  <list_name> value          lrange <list_name> start end
    Set                                 sadd  <set_name>  value          smembers <setname>
    Zset 有序集合                          zadd <zset_name> score member  zrangebyscore  <zset_name> score end  zset_name,menber 不能重复 score可以重复

"""

import redis

pool=redis.ConnectionPool(host="127.0.0.1",port=6379)
r=redis.Redis(connection_pool=pool)
for i in uuids:
    r.lpush("id",i)
print (r.lrange("id","0",len(uuids)))

