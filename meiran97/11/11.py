# 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。


with open('敏感词.txt', 'r') as f:
    filter = [line.rstrip() for line in f]  # 注意这里的简便写法
# print(filter)

i = input('》')
if i in filter:
    print('Freedom')
else:
    print('Human Rights')
