f = open('filtered_words.txt')
data = f.read()

wordlist = data.split('\n')

def inspector(input_line):
    flag = False
    for word in wordlist:
         if input_line.find(word)>=0:
             flag = True
             break
         else:
             pass
    if flag == True:
        print 'Freedom'
    else:
        print 'Human Rights'

while True:
    input_line = raw_input('>')
    inspector(input_line)
