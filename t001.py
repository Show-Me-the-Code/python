#-*-coding utf-8-*-
import random, string

def generateCode(length):
    a = ''
    print(a)
    numbox = range(48,58), range(65, 91), range(97, 123)
    #print (numbox)
    for i in range(length):
        m = random.randint(0,2)
        if m == 0:
            n = random.randint(0,9)
        else:
            n = random.randint(0,23)

        #print([chr(numbox[m][n])])
        a = a + chr(numbox[m][n])
    #print(a)
    return a

Code_num = 200
code = []
for i in range(Code_num):
    code =code + [generateCode(10)]

print(code)
