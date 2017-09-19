# from collections import Counter
# import re
#
#
# def creat_list(filename):
#     datalist = []
#     with open(filename, 'r') as f:
#         for line in f:
#             content = re.sub("\"|,|\.", "", line)
#             datalist.extend(content.strip().split(' '))
#     return datalist
#
#
# def wc(filename):
#     print Counter(creat_list(filename))
#
# if __name__ == "__main__":
#     filename = 'test.txt'
#     wc(filename)


fileName = 'file.txt'

fileOpen = open(fileName,'r')

content = fileOpen.read()

counter = 0

for i in content.split(' '):
    counter = counter + 1

print counter

fileOpen.close()

