from hashlib import sha256
from hmac import HMAC
import os


class Encrypt(object):

    def encrypt(self, password, salt=None):
        if salt is None:
            salt = os.urandom(8)
        result = password.encode('utf-8')
        for i in range(10):
            result = HMAC(result, salt, sha256).digest()
        return salt + result

    def vaildate(self, password, hashed):
        return hashed == self.encrypt(password, salt=hashed[:8])

if __name__ == '__main__':
    obj = Encrypt()
    hashed = obj.encrypt('wh5622')
    # print(bytes.decode(hashed))
    ans = obj.vaildate('wh5622', hashed)
    print(ans)
