"""

# Program 1: to display the Fibonacci sequence up to user entered n-th term

nterms = int(input("How many terms? "))

# for first two terms
n1, n2 = 0, 1
count = 0

# to check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1



# Program 2: A year is a leap year if it is divisible by 4,
# except that years divisible by 100 are not leap years unless they are also divisible by 400.
# Ask the user to enter a year, and, using the // operator, determine how many leap years there have been between 1600 and that year.


start = int(input("enter the start year:"))
end = int(input("enter the last year:"))

count = 0

for year in range(start, end):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        count += 1




"""
Program 3:



"""



def print_perfect_nums(start, end):
   for i in range(start, end + 1):
    sum = 0
    for x in range(1, i):

      # to Check if has a divisor, if it has, add to sum

        if(i % x == 0):
            sum = sum + x
            if (sum == i):
                print(i)
print_perfect_nums(1, 1000)


"""
Write a program that swaps the values of three variables x, y, and z,
so that x gets the value of y, y gets the value of z, and z gets the value of x.

"""
x = int(input("Enter the first number to swap:"))

y = int(input("Enter the second number to swap:"))

z = int(input("Enter the third number to swap:"))

print("The value of x , y and z before swapping is:",x,y,z)

temp = x
x = y
y = z
z = temp

print("The value of x , y and z after swapping is:",x,y,z)




"""
 At a certain school, student email addresses end with @student.sharda.edu,
 while professor email addresses end with @prof.sharda.edu.
 Write a program that first asks the user how many email addresses they will be entering,
 and then has the user enter those addresses.
 After all the email addresses are entered, the program should print out a message indicating
 either that all the addresses are student addresses or that there were some professor addresses entered.

"""

maxlength = int(input("Enter the maximum number of inputs:\n"))

a = []

while len(a)<maxlength:
    a1=input("enter the ID:\n")
    a.append(a1)

print(a)

for i in a:
    splitword = i.split("@")
    if (splitword[1]=='student.sharda.edu'):
        print("Student ID")

    else:
        print("Professor ID ")