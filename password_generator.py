small ='a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z''A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S',"T","U","V","W","X","Y","Z"
speci_char= "!","@","#","$","%","^","&","*","(",")","/","+","-0"
num="1","2","3","4","5","6","7","8","9"
import random

password =""
# length= int (input ("length of your password"))
alpha_len= int (input("how many alphabets you want in your password "))
special = int (input("how many special characters you want"))
num_length=int (input("how many number you want in your password"))

    # for i in range(length+1):
for j in range(alpha_len+1):
    e= random.choice(small)
    password+=e

for j in range(special+1):
    e= random.choice(speci_char)
    password+=e

for j in range(num_length+1):
    e = random.choice(num)
    password+=e

print(password)


