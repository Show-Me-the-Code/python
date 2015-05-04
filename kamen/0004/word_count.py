from collections import Counter
#collections
#counter + - & | most_common
with open('a.txt', 'r') as f:
    c=Counter()
    for line in f:
        line_list=line.split()
        c+=Counter(line_list)

print c.most_common()
        
