# Python code to calculate number 
# of ways of selecting \'p\' non 
# consecutive stations out of 
# \'n\' stations 

def stopping_station( p, n): 
	num = 1
	dem = 1
	s = p 

	# selecting \'s\' positions 
	# out of \'n-s+1\' 
	while p != 1: 
		dem *= p 
		p-=1
	
	t = n - s + 1
	while t != (n-2 * s + 1): 
		num *= t 
		t-=1
	if (n - s + 1) >= s: 
		return int(num/dem) 
	else: 
		# if conditions does not 
		# satisfy of combinatorics 
		return -1

# driver code 
num = stopping_station(4, 12) 
if num != -1: 
	print(num) 
else: 
	print("Not Possible") 

# This code is contributed by "Abhishek Sharma 44" 
