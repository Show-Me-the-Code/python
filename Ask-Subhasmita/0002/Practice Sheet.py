
"""
#PROGRAM 1:Demonstrate how will you find numbers divisible by nine or three from a user input list of numbers using Lambda.

lst = []     #takes an empty list to store the elements entered by the user

for i in range(0,4):
    n = int(input("Enter the elements:"))  #applying loop to take elements from the user
    lst.append(n)

print(lst)

res_lst = list(filter(lambda n1:(n1%3 == 0 or n1%9 == 0), lst))  #function to check divisibility

print(res_lst)  #print result



#PROGRAM 2:Write a Python program to create a lambda function that adds 20 to a given number passed in as an argument,
#also create a lambda function that multiplies argument x with argument y and print the result.


n = lambda m:m+20         #attribute lambda to call the one time function
print("addition :",n(100))

n1 = lambda x,y:x*y
print("multiplication:",n1(99,67))




#PROGRAM 3:Demonstrate with the help of Python code by using lambda function to find the intersection of two given arrays. Take array from user.

print("ENTER THE ARRAY ELEMENTS WITH SPACES!\n")

print("Enter first array elements: ")                        #getting array elements
array_nums1 = [int(i) for i in input().split()]

print("Enter second array elements: ")
array_nums2 = [int(i) for i in input().split()]

print("Original arrays:")
print(array_nums1)
print(array_nums2)
result = list(filter(lambda x: x in array_nums1, array_nums2))         #applying lambda function to get the intersction of two arrays
print ("\nIntersection of the said arrays: ",result)          #result



#PROGRAM 4:With the help of Python program, find all anagrams of a string in a given list of strings using lambda.Please read the definition of anagrams from wikipedia.


from itertools import groupby

test_list = ['lump', 'eat', 'me', 'tea', 'em', 'plum']    # initializing list

print("The original list : " , str(test_list))  # printing original list

sorted_list = lambda test_list: sorted(test_list)      # Grouping Anagrams

result_list = [list(val) for key, val in groupby(sorted(test_list, key = sorted_list), sorted_list)]

print("The grouped Anagrams : " + str(result_list))  # print result



#PROGRAM 5:By using the concept of recursion ,calculate the value of 'c' to the power 'd'.

def power(a,b):         #defining the function with arguments
    if a == 0:
        return 1
    else:
        return a**b

print(power(7,8))    #recurring function
print(power(9,5))

"""

#PROGRAM 6:Write a Python program of the sum of all the elements in the list(user input). Use the concept of recursion.

from functools import reduce

print("Enter the elements separated by spaces: ")
n = [int(i) for i in input().split()]

print(n)

sum = reduce(lambda x,y:x+y ,n)

print("sum of all elements:",sum)




