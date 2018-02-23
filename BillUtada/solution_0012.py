#coding=UTF-8
import string
import sys
reload(sys)
sys.setdefaultencoding("utf8")

#config
FILTERED_WORDS_PATH = '/Users/billutada/pythonPractice/Sources/filtered_words'

if __name__ == '__main__':
    bad_word_ls = [];
    with open(FILTERED_WORDS_PATH, 'r') as f:
        bad_word_ls = f.read().splitlines();
        word = raw_input();
        flag = False;
        for bad_word in bad_word_ls:
            if bad_word in word:
                if(u'\u4e00' <= unicode(bad_word, 'utf-8')[0] <= u'\u9fff'):
                    word = word[:word.find(bad_word)] + '*' * (len(bad_word)/3) + word[word.find(bad_word)+len(bad_word):];
                else:
                    word = word[:word.find(bad_word)] + '*' * len(bad_word) + word[word.find(bad_word)+len(bad_word):];
        print word;
