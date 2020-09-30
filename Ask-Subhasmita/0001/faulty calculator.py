#faulty calculator

print("Enter your first number")
n1=int(input())
print("Enter your second number")
n2=int(input())
print("Choose your operator")
op = input('''
    Please type in the math operation you would like to complete:
    + for addition
    - for subtraction
    * for multiplication
    / for division
    ** for power
    % for modulo

    Enter Your Choice:
    ''')

    if op=='+':
        if n1==56 and n2==9:
       print("56+9=77")
    else:
       print(n1+n2)
    if op=='-':
    if n1==89 and n2==68:
        print("89+68=171")
    else:
        print(n1-n2)
        if op=='*':
    if n1==5 and n2==6:
        print("5*6=25")
    else:
        print(n1*n2)
        if op=='/':
    print(n1/n2)
if op=='**':
    print(n1**n2)

else:
    print("error! please choose a correct option")


