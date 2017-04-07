import random
import string


# this method use the 'key' to select 10 random characters
def generateCode(count):
    for code in range(count):
        key = string.upper('0123456789abcefghijklmnopqrstuvwxyz')
        code = string.join(random.sample(key, 10))
        print(code)

generateCode(10)    # generate the amount of codes you send as count
