fname = input('Enter the file name:')
fhand = open(fname)##file handle to open the file.

count = 0

for line in fhand:##to iterate through the num of lines in file.
    line = line.rstrip()
    if line.startswith('coupon'):
        count = count + 1
    print(line[13:25])##to parse and get the coupon code.
print('There are', count ,'coupon' )
