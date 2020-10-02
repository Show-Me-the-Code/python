fptr = open("file.txt","r+")
words = fptr.read().split(" ")
print(len(words))
