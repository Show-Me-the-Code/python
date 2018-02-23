import string

#config
BADWORDPATH = '/home/william/pythonPractice/Sources/filtered_words'

if __name__ == '__main__':
    bad_word_ls = [];
    with open(BADWORDPATH, "r") as f:
        bad_word_ls = f.read().splitlines();
        word = raw_input();
        flag = False;
        for bad_word in bad_word_ls:
            if bad_word in word:
                print 'Freedom';
                flag = True;
                break;
        if not flag:
            print 'Human Rights';
