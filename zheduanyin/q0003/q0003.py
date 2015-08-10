# 存入redis
import redis
import torndb


def read_db(host='127.0.0.1', database='showmethecode', table='q2_keyset', user='root', password='', charset='utf8mb4'):
    db = torndb.Connection(
        host=host,
        database=database,
        user=user,
        password=password,
        charset=charset,
    )
    return db.query('select * from {table}'.format(table=table))

if __name__ == '__main__':
    r = redis.StrictRedis(host='localhost', port=6379)
    keyset_dict = {}
    for key in read_db():
        keyset_dict.update({key['id']: key['key']})
    r.mset(keyset_dict)
