#!/usr/bin/python

# 获取敏感词汇
def get_words(filename):
  with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
    pilter = [line.rstrip() for line in f.readlines()]
    print(pilter)
    return pilter
    
# 获取输入的关键字
input_word = input("请输入关键字:")

# 关键字判断
def input_result(filename):
  result = get_words(filename)
  if input_word in result:
    print('Freedom')
  else:
    print('Human Rights')
  

if __name__ == '__main__':
  input_result('filtered_words.txt')
