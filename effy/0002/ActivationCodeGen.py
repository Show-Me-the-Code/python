#!/usr/bin/env
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
