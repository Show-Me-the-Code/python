try:
    age= int(input("enter your age"))
    if age< 18:
        print("minor")
    else:
        print("major")
except:
    print("age is not valid")