# 存入mysql

import torndb

from q0001 import generate_keyset


if __name__ == '__main__':
    conn = torndb.Connection(
        host='127.0.0.1',
        database='showmethecode',
        user='root',
        password='',
        charset='utf8mb4'
    )

    keyset = generate_keyset(16, 200, True)
    conn.executemany('insert q2_keyset(`key`) values(%s)', keyset)
