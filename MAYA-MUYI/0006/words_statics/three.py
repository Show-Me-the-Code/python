import os
import string

def count_words(dirpath):
    if not os.path.isdir(dirpath):
        print('please input legal dirpath!')
        return

    exclude_words = ['a', 'an', 'the', 'and', 'or', 'of', 'in', 'at', 'to', 'is','…', '–' ]
    table = str.maketrans("", "", string.punctuation)
    for root, dirs, files in os.walk(dirpath):
        for name in files:
            filename = os.path.join(root, name)
            if not os.path.isfile(filename) or not os.path.splitext(filename)[1] == '.txt':
                print('diary < %s > format is not .txt' % filename)
                return
            f = open(filename, 'r', encoding='utf-8')
            data = f.read()
            # words = re_obj.findall(data)
            words = data.translate(table).split()
            word_dict = dict()
            n = 0
            for word in words:
                word = word.lower()
                if word[-1] == '-':
                    m = word[:-1]
                    n = 1
                    break
                if n == 1:
                    word = m + word
                    n = 0
                if word in exclude_words:
                    continue
                if word in word_dict:
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1
            f.close()
            word_dict = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
            print('The most word in diary < %s > is: %s' % (name, word_dict[0]))

if __name__ == '__main__':
    count_words('diary')

