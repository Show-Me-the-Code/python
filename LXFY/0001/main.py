import random, string

f = open('Promo_code.txt', 'wb')
for i in range(200):
    chars = string.letters + string.digits
    s = [random.choice(chars) for i in range(10)]
    f.write(''.join(s) + '\n')
f.close()