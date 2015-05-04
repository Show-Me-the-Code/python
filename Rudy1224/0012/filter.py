f = open('filtered_words.txt')
data = f.read()

wordlist = data.split('\n')

def word_filter(input_line):
    for word in wordlist:
        if input_line.find(word) == -1:
            pass
        else:
            input_line = input_line.replace(word, '*' * (len(word)/2))
    print input_line

while True:
    input_line = raw_input('>')
    word_filter(input_line)
