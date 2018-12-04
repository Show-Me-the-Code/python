## 第 0006 题

你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。

## count_words.py

注意点：

1、都是 txt 文件，非该格式的日志要排除

2、去除非常常见的介词，如`of` 等

日志都在文件夹 `diary` 中，运行结果如下：

```
▶ python3 count_words.py
The most word in diary < 1.txt > is: ('you', 7)
The most word in diary < 2.txt > is: ('this', 4)
The most word in diary < 3.txt > is: ('with', 7)
diary < diary\4.cc > format is not .txt
```

## 知识点学习

**sorted函数**

`sorted()` 函数是一个高阶函数，可以接受一个 `key` 函数来实现自定义排序，同时还可以通过第三个参数 `reverse=True` 来实现反向排序。

```
word_dict = sorted(word_dict.items(), key = lambda x: x[1], reverse = True)
```

**匿名函数`lambda`**

格式：

```
lambda [parameters]: commands
```

当一些函数很简单，仅仅只是计算一个表达式的值的时候，可以使用lambda表达式来代替。比如，为sorted() 创建一个很短的回调函数，又不想用 `def` 去写一个单行函数，而是希望通过这个快捷方式以内联方式来创建这个函数。

尽管lambda表达式允许定义简单函数，但是它的使用是有限制的。 只能指定单个表达式，它的值就是最后的返回值。也就是说不能包含其他的语言特性了， 包括多个语句、条件表达式、迭代以及异常处理等等。

- 其他
  1. one.py 用简单正则抓取words.txt下的单词，但无法忽略标点符号或者单词拼接等问题
  2. two.py 同样的用正则抓取单词，但是增加了符号和拼接处理
  3. three.py 在前两者的基础上做了改良，用了比正则更加简单迅速的string处理模块。主要利用translate和punctuation处理，简单迅速，几行代码就可以实现对文本的处理