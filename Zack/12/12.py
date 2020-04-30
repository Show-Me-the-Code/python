'''
第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，
则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
'''

with open('敏感词.txt', 'r') as f:
    words = [i.strip() for i in f.readlines()]

user_input = input('>')
for word in words:
    if word in user_input:
        output = user_input.replace(word, '*'*len(word))
print(output)