#-*- coding:utf-8 -*-
import uuid
from itertools import dropwhile

def generateActivationCode(num):
    codeList = []
    for i in range(num):
        code = str(uuid.uuid4()).replace('-','').upper()
        while code in codeList:
            code = str(uuid.uuid4()).replace('-','').upper()
        codeList.append(code)

    for code in codeList:
        print(code)

if __name__ == '__main__':
    generateActivationCode(200)

#output
# 4A5C6F8482544BA8B61F26945E8DA6CA
# 002751306CA34E798BE492379F14F09B
# AD2FD3F1C5CC4769AA3C9FF1D9247C77
# BB9BB4D6B4AC490A800929B7ABA0CF48
# 28F0A9E062964313B36556A6D4B62753
# 1C5D17EF07FC484B8DADB15FAC0D9BB5
# AC2146D68BA34199B75ACC727D2B017D
# 64866B2136C641DA956A3A52274DA3E0
# F00DDD20295C4E2CBDC8E62A0C72AABC
#...