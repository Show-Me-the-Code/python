#  敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights


def read_file(file_path):
    file = open(file_path, 'r')
    words = []
    for word in file.readlines():
        # print(word.strip('\n'))
        words.append(word.strip('\n'))
    file.close()
    return words


def check(word, file_path):
    real_words = read_file(file_path)
    for i in real_words:
        if i == word:
            return 'Freedom'
    else:
        return 'Human Rights'


response = check('hello', 'filtered_words.txt')
print(response)
