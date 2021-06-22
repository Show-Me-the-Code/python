# 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」


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
        if word.__contains__(i):
            return word.replace(i, '*' * len(i))
    else:
        return word


response = check('北京是个好城市', 'filtered_words.txt')
print(response)
