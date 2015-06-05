import io

file = io.open('filtered_words.txt', 'r')
list = []
for word in file.readlines():
    list.append(word.strip('\n'))

print(list)

def isValid(mystr):
    result = mystr
    for x in list:
        if result.find(x) != -1:
            result = result.replace(x, '**')
    return result

mystr = input("please input a string:")
print (isValid(mystr))

file.close()
