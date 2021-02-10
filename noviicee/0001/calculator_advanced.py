#advanced calculator
#a calculator with some more advanced features..
#it will work until we exit the calculator

import sys
#define functions for the advanced calculator-
def add(x,y):
	return (x+y)

def subtract(x,y):
	return (x-y)

def multiply(x,y):
	return (x*y)

def get_modulus(x,y):
	return(x%y)

def float_divide(x,y):
	return (x/y)

def floor_divide(x,y):
	return(x//y)

#take input from the user
while True:
	choice=int(input("""Select Operation:\n
		1.Add
		2.Subtract
		3.Multiply
		4.Get the Remainder after division
		5.Divide
		6.Divide and get the integer value
		7. Exit\n\n"""))
	if choice == 1:
		num1 = int(input("Enter first number: \n"))
		num2 = int(input("Enter second number: \n"))
		print(num1,"+",num2,"=", add(num1,num2))
	elif choice == 2:
		num1 = int(input("Enter first number: \n"))
		num2 = int(input("Enter second number: \n"))
		print(num1,"-",num2,"=", subtract(num1,num2))
	elif choice == 3:
		num1 = int(input("Enter first number: \n"))
		num2 = int(input("Enter second number: \n"))
		print(num1,"*",num2,"=", multiply(num1,num2))
	elif choice == 4:
		num1 = int(input("Enter first number: \n"))
		num2 = int(input("Enter second number: \n"))
		print(num1,"%",num2,"=", get_modulus(num1,num2))
	elif choice == 5:
		num1 = int(input("Enter first number: \n"))
		num2 = int(input("Enter second number: \n"))
		print(num1,"/",num2,"=", float_divide(num1,num2))
	elif choice == 6:
		num1 = int(input("Enter first number: \n"))
		num2 = int(input("Enter second number: \n"))
		print(num1,"//",num2,"=", floor_divide(num1,num2))
	elif choice==7:
		sys.exit(0)
	else:
		print("Invalid input.")
		print("Try Again...")
