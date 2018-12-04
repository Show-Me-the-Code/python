import random
import string


def gen_string(number, width, filename):
    str = string.digits + string.ascii_letters
    f = open(filename, 'w')
    for i in range(number):
        temp_verify = [random.choice(str) for i in range(width)]
        verify = ''.join(temp_verify) + '\n'
        f.write(verify)
        print(verify)

if __name__ == '__main__':
    number = eval(input("请输入所要生成的验证码的个数"))
    width = eval(input("请输入验证码位数"))
    filename = input("请输入保存的文件名")
    gen_string(number, width, filename)