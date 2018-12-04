
def filter_word(filename):
    #打开定义好规则的文本
    f = open(filename, 'r', encoding='utf-8')
    将每行内容读取并存为一个列表
    rules = [line.strip() for line in f]
    while True:
        words = input('please input your word：\n')
        if words == 'exit':
            break

        print('the result is: ')
        for rule in rules:
            if rule in words:
                #将存在于规则列表内的字段替换为*
                words = words.replace(rule, '*' * len(rule))
        print("the result is : ", words)
        print("——————————————————————————")



if __name__ == '__main__':
    filter_word('filtered_words.txt')