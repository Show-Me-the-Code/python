#count the frequency of each word or number( namely not space character)
import string, re


def count_word(filename):
    f = open(filename, 'rb')
    wdic = {}
    for line in f:
        line = line.lower().strip()
        #split by regular expression, more powerful function
        words = re.split('\W+', line)
        #words = re.findall('[a-zA-Z0-9]+', line)
        
        for word in words:
            if word in wdic:
                wdic[word] += 1
            else:
                wdic[word] = 1
    f.close()
    #sort by frequency
    #Returns a new sorted list with (key, value) pairs, dict cannot be sorted
    wdic = sorted(wdic.items(), key = lambda x: x[1], reverse = True)
    print wdic

if __name__ == '__main__':
    filename = 'testtext.txt'
    count_word(filename)
