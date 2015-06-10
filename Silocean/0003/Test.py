# -*-coding:utf-8-*-
__author__ = 'Tracy'
import redis, uuid

r = redis.StrictRedis(host='localhost', port=6379)
for i in range(200):
    r.set('key_id'+str(i), uuid.uuid1())

for i in range(200):
    print(r.get("key_id"+str(i)))