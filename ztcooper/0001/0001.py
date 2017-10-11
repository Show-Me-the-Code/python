import uuid

keys = []
for i in range(200):
    key = uuid.uuid4()
    keys.append(key)

with open('keys.txt', 'w') as f:
    for key in keys:
        f.write(str(key) + '\n')
