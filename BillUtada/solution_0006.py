import os
import solution_0004
import string

#config
DAILY_PATH = './Sources/daily/'
FILTERED_WORD = list(string.letters) + ['later', 'not', 'pm', 's', 'i', 'to', 'go', 'went', 'goes', 'she', 'her', 'he', 'his', 'am', 'is', 'are', 'have', 'will', 'has', 'had', 'the', 'in', 'of', 'a', 'an', 'that', 'this', 'with', 'as', 'and', 'at', 'does', 'do', 'you', 'your', 'my'];

def find_most_important_word(daily):
    with open(DAILY_PATH + daily, "r") as f:
        word_statics = solution_0004.anlsText(f.read());
        for fw in FILTERED_WORD:
            if fw in word_statics:
                del word_statics[fw];
        res = sorted(word_statics.items(), reverse = True, key = lambda x : x[1]);
        return ("the most important word in %s is   %s" % (daily, res[0][0]));


if __name__ == '__main__':
    for f in os.walk(DAILY_PATH).next()[2]:
        print find_most_important_word(f);
