## 第 0001 题
做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？

## 生成所有字母
python 2.7 中的函数是：`string.letters`
python 3 中的函数是：`string.ascii_letters`

## 生成所有数字
函数 `sring.digits` 可以实现

## choice函数

**功能**
choice() 方法返回一个列表，元组或字符串的随机项。
```
import random
random.choice( seq  )
```

seq -- 可以是一个列表，元组或字符串

>注意：choice()是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法。

## string.join()

Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。

```
str.join(sequence)
```

例子

```
str = "-";
seq = ("a", "b", "c"); # 字符串序列
print str.join( seq );
```

输出

```
a-b-c
```

## python3代码的改动

1、没有 string.letters 这个函数，取而代之的是 string.ascii_letters

2、open的时候不要加`b` 选项，否则会出错 `TypeError: a bytes-like object is required, not 'str'` 。
原因是当前操作的字符串是bytes类型的字符串对象，并对该bytes类型的字符串对象进行按照str类型的操作。
str 和 bytes 类型之间需要转码
