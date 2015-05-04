#### 说明： ####

对自然语言处理没有接触过，因此第0006题，我只是简单地处理

1，首先，将txt读入，并且去除stopwords(english)，stopwords在NLTK这个包中有现成，进行词频统计。
2，其次，选择词频最高的三个

ps：读入文件时，判断后缀用endswith('.txt')；os.listdir()读当前目录文件

网络上搜到Shlomi Babluki的一篇blog，讲述了如何从一个句子提取出topic，我改了下他的基本代码，见![头像](extract_key_word_Shlomi_Babluki.py),个人感觉比我自己简单地进行词频统计要有效的多，它做了一些句子成分的分析考虑，不是很懂，但是柑橘很有用。