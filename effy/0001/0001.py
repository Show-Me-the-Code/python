#!/usr/bin/env
'''
Self-defined activation code

1. has length of 10
2. mixture of letters and numbers
3. unique throughtout 200 combos

Pros: 
total of 3656158440062976 combos, randomly generation of 200 is almost 
guaranteed to be unique; Confident level if high without look up opeations.
And without look up, it's super fast :) The more codes needed, the effect 
is more obvious.

Cons: 
Without back tracking, small chance would occur of duplication.
'''
import random

codeSeedA = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def digit(raw):
	l = len(raw)
	return raw[random.randrange(l)] 

def codeGen(n):
	codes_pool = []
	for i in range(n):
		code = ""
		for i in range(10):
			code += digit(codeSeedA)
		codes_pool.append(code)
	return codes_pool

'''
Standard uuid
'''
import uuid
def uuidGen(n):
	codes_pool =[]
	for i in range(n):
		codes_pool.append(uuid.uuid4())
	return codes_pool

#codes_udf = codeGen(10000)
codes_uuid = uuidGen(10000)


'''
In the case of 200 activation code, it is almost equally fast.

As the size of code pool grows (e.g. to 10000), uuidGen() is twice slower than codeGen(),
since uuid is checking whether duplications. Plus, the confidence level of codeGen() to not
produce duplication lowers down as pool size increases.

'''