# Why Python Is Great:
# In-place value swapping

# Let's say we want to swap the values of a and b...
a = 23
b = 42

"""
# The "classic" way to do it with a temporary variable:
tmp = a
a = b
b = tmp
"""

# Python also lets us use this short-hand:
a, b = b, a

print("", a, "\n", b)

"""
Output:

42
23
"""
