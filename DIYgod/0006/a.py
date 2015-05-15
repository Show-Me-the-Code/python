f = open('a.txt', 'rb')
lines = f.readlines()
for line in lines:
    pass
f.close()

f = open('a.txt', 'rb')
for line in f:
    pass
f.close()

f = open('a.txt', 'rb')
while true:
    line = f.readline()
    if not line:
        break
    pass
f.close()
