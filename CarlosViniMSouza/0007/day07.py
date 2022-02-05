# The "timeit" module lets you measure the execution
# time of small bits of Python code

import timeit

t1 = timeit.timeit('"-".join(str(n) for n in range(100))', number=100)
print(t1)

# Output: 0.0013168999976187479

t2 = timeit.timeit('"-".join([str(n) for n in range(100)])', number=100)
print(t2)

# Output: 0.0012954000012541655

t3 = timeit.timeit('"-".join(map(str, range(100)))', number=100)
print(t3)

# Output: 0.0011196999985259026
