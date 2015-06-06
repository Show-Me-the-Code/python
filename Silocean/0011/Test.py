import io

file = io.open('filtered_words.txt', 'r')
list = []
for word in file.readlines():
    list.append(word.strip('\n'))

print(list)

def isValid(word):
    for x in list:
        if word == x:
            return False
    return True

myword = input("please input a word:")
if isValid(myword):
    print('Human Rights')
else:
    print('Freedom')

file.close()
