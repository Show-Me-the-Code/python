# How to sort a Python dict by value

import operator


dict_test = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

print(sorted(dict_test.items(), key=lambda x: x[1]))
# Ouput: [('d', 1), ('c', 2), ('b', 3), ('a', 4)]

print(sorted(dict_test.items(), key=operator.itemgetter(1)))
# Output: [('d', 1), ('c', 2), ('b', 3), ('a', 4)]
