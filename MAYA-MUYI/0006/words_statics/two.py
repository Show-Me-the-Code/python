import re
def get_word_frequencies(file_name):
    dic = {}
    txt = open(file_name, 'r').read().splitlines()

    n=0
    for line in txt:
        print(line)
        line = re.sub(r'[.?!,""/]', ' ', line)   #要替换的标点符号，英文字符可能出现的
        line = re.sub(r' - ', ' ', line) #替换单独的‘-’
        for word in line.split():

            #当一行的最后一个字符是-的时候，需要跟下一个英文字符串联起来构成单词
            if word[-1] =='-':
                    m=word[:-1]
                    n=1
                    break
            if n==1:
                word=m+word
                n=0
            # print(word)
            dic.setdefault(word.lower(), 0)  #不区分大小写
            dic[word.lower()] += 1
    print(dic)
    print("单词总数:", len(dic))

if __name__ == '__main__':
    get_word_frequencies('words.txt')