n = int(input())
c = 0
d = 0
x = 0
for i in range(n):
    e = input()
    a,b = e.split()
    c += int(a)
    d += int(b)
x = d//1000
c += x
print(c, "(in liters)")
print(d-x*1000, "(in ml)")
