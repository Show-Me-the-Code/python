# 写入 excel
import sys
sys.path.append('..')
from q0014.q0014 import copy_json_into_excel


if __name__ == '__main__':
    data = copy_json_into_excel('numbers.txt')
