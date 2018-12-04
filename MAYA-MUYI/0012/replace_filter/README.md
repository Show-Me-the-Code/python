## 第 0012 题

敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。

## replace_fiter_word.py

**测试结果:**

```
▶ python replace_filter_word.py
please input your word:
北京是个好城市
the result is:
**是个好城市
please input your word:
公务员是未来的贪官
the result is:
***是未来的贪官
please input your word:
I want to have sex now
the result is:
I want to have *** now
please input your word:
today is sunday, 睡觉睡觉
the result is:
today is sunday, 睡觉睡觉
please input your word:
exit
```

**`replace()`**

replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。

```
str.replace(old, new[, max])
```

- old -- 将被替换的子字符串。

- new -- 新字符串，用于替换old子字符串。

- max -- 可选字符串, 替换不超过 max 次
