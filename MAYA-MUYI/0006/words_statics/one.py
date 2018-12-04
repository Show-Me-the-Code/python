import re

def word_count(fileneme):
    f = open(fileneme, 'r')
    str = f.read()
    re_obj =re.compile('\b?(\w+)\b?')
    words = re_obj.findall(str)
    f.close()

    word_dict = dict()
    for word in words:
        if word.lower() in word_dict:
            word_dict[word.lower()] += 1
        else:
            word_dict[word.lower()] = 1

    for key, value in word_dict.items():
        print('%s: %s' % (key, value))

if __name__ == '__main__':
    word_count('words.txt')