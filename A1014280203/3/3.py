import redis
import base64
import re


def make_connect():
    r = redis.Redis(host='', port=)
    return r


def parse_coupon(c_code):
    return base64.urlsafe_b64decode(c_code.encode('utf-8'))


def upload_to_database():
    session = make_connect()
    with open('coupon.txt', 'r') as file:
        for line in file.readlines():
            c_id = re.findall(r'.*/.*:(.*)\'', str(parse_coupon(line)))
            session.set(c_id.pop(), line.strip())

if __name__ == '__main__':
    upload_to_database()
