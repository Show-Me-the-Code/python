**第 0023 题：** 使用 Python 的 Web 框架，做一个 Web 版本 留言簿 应用。

[阅读资料：Python 有哪些 Web 框架](http://v2ex.com/t/151643#reply53)

- ![留言簿参考](http://i.imgur.com/VIyCZ0i.jpg)
---------------------------------------

以前在sea上弄过一个差不多的：http://www.jithee.name/guestbook/
不过sea弄django syncdb比较痛苦，所有sql拼接出的
直接django真够傻瓜的……

代码版本用的sqlite3，本地调试的时候用的mysql

    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'guestbook',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
