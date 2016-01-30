import re
import string


class Filter(object):

    def __init__(self):
        self.filtered_word_list = []
        self.readIO()

    def check(self, word_input):
        res = word_input
        for e in self.filtered_word_list:
            # print(e)
            if e in word_input:
                res = res.replace(e, '*' * len(e))
        return res

    def readIO(self):
        with open('demo.txt', 'r') as f:
            s_temp = f.readline().strip()
            while s_temp != "":
                self.filtered_word_list.append(s_temp)
                s_temp = f.readline().strip()

if __name__ == "__main__":
    filter_obj = Filter()
    while True:
        word_input = input("Enter a sentence to check >")
        str_ans = filter_obj.check(word_input)
        print(str_ans)
