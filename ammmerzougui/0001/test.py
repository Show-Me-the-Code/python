'''
Generating a random code 
By @ammmerzougui
'''
import random

def genCode(length):
	s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
	return "".join(random.sample(s,length))
l=input("Enter the length of the random code: ")
print(genCode(int(l)))
