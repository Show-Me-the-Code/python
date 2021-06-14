# 将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。

import redis

r = redis.StrictRedis(host='localhost', port=6379)

with open('../0001/txt/activate_code.txt', 'r') as f:
    activate_codes = f.readlines()
    for i in range(0, 200):
        r.set('activate_code:' + str(i), activate_codes[i])

for i in range(0, 200):
    print(r.get("activate_code:" + str(i)))

r.close()
