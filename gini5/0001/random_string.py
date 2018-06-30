import random, string

dic = {}

def generate_string(size=8):
    seed = string.ascii_letters+string.digits
    res = ''.join(random.sample(seed,size))
    return res

for i in range(200):
    new = generate_string()
    while new in dic.values():
        new = generate_string()
    dic[i] = new

print(dic)
