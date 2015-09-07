__author__ = 'karnikamit'
'''
Project Euler problem #1
Multiples of 3 and 5
'''

print sum([i for i in xrange(1000) if i % 3 == 0 or i % 5 == 0])
