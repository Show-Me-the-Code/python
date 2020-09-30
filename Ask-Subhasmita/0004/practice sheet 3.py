#1.WRITE A PYTHON PROGRAM TO DISPLAY ASTROLOGICAL SIGN FOR GIVEN DATE OF BIRTH.

day = int(input("Input birthday: "))
month = input("Input month of birth (e.g. march, july etc): ")
if month == 'december':
	astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'
elif month == 'january':
	astro_sign = 'Capricorn' if (day < 20) else 'aquarius'
elif month == 'february':
	astro_sign = 'Aquarius' if (day < 19) else 'pisces'
elif month == 'march':
	astro_sign = 'Pisces' if (day < 21) else 'aries'
elif month == 'april':
	astro_sign = 'Aries' if (day < 20) else 'taurus'
elif month == 'may':
	astro_sign = 'Taurus' if (day < 21) else 'gemini'
elif month == 'june':
	astro_sign = 'Gemini' if (day < 21) else 'cancer'
elif month == 'july':
	astro_sign = 'Cancer' if (day < 23) else 'leo'
elif month == 'august':
	astro_sign = 'Leo' if (day < 23) else 'virgo'
elif month == 'september':
	astro_sign = 'Virgo' if (day < 23) else 'libra'
elif month == 'october':
	astro_sign = 'Libra' if (day < 23) else 'scorpio'
elif month == 'november':
	astro_sign = 'scorpio' if (day < 22) else 'sagittarius'
print("Your Astrological sign is :",astro_sign)



#2. WRITE A PYTHON PROGRAM TO CHECK A TRIANGLE IS EQUILATERAL , ISOSCELES OR SCALENE

x = int(input("ENTER THE FIRST SIDE OF THE TRIANGLE:"))

y = int(input("\nENTER THE SECOND SIDE OF THE TRIANGLE:"))

z = int(input("\nENTER THE THIRD SIDE OF THE TRIANGLE:"))

if (x==y) & (y==z):
    print("\nTRIANGLE IS EQUILATERAL")

elif (x==y)&(x!=z):
    print("\nTRIANGLE IS ISOSCELES")
elif (x==y) or (y==z) or (z==x):
    print("triangle is isosceles")
elif (y==z)&(z!=x):
    print("\nTRIANGLE IS ISOSCELES")

else:
    print("\nTRIANGLE IS SCALENE")

# 3.WRITE A PYTHON PROGRAM TO READ ALL THREE NUMBERS a,b,c AND CHECK HOW MANY NUMBERS BETWEEN 'a' AND 'b' ARE DIVISIBLE BY 'c'

a = int(input("enter 1st number:"))
b = int(input("\nenter 2nd number:"))
c = int(input("\nenter 3rd number:"))
n = 0
for x in range(a+1,b):
    if x%c==0:
        n = n+1

print(n)

"""

#4.WRITE A PYTHON PROGRAM TP PRINT ALL PRIME NUMBERS BETWEEN 0 TO 100 AND PRINT HOW MANY PRIME NUMBERS ARE THERE


for Number in range (0, 101):
    count = 0
    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            count = count + 1
            break

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '  ')









