#My Repository
##My-Solutions-For-Show-Me-the-Code
https://github.com/houshengandt/My-Solutions-For-Show-Me-The-Code
##关于第0025题百度语音解法
https://github.com/houshengandt/My-Solutions-For-Show-Me-The-Code/blob/master/0025/help.md

###使用方法
`python3 0025.py`

在 输出 正在录音...... 时喊出你想打开的网站，录音时间有5秒，之后会上传。
目前支持“百度”“微博”“谷歌”，可以在代码中的dict website 里添加你想要的网站，但注意识别不是百分百准确，每个人口音也有差异，根据识别结果来调整value值。

######题目
[Python 练习册，每天一个小程序](https://github.com/Yixiaohan/show-me-the-code)
>第 0025 题： 使用Python实现：对着电脑吼一声,自动打开浏览器中的默认网站。
>
>例如，对着笔记本电脑吼一声“百度”，浏览器自动打开百度首页。
>
> 关键字：Speech to Text



PyAudio是唯一一个用到的外部库，用来录制音频文件，官方的[录音实例](http://people.csail.mit.edu/hubert/pyaudio/#record-example)可以直接拿来使用。

使用 百度语音识别 REST API：
* [官方文档](http://yuyin.baidu.com/docs/asr/56)
* [access_token的获取](http://developer.baidu.com/wiki/index.php?title=docs/oauth/client)
* 注意，“百度”会被识别为“ｂａｉｄｕ，”，即使返回“百渡”也不回“百度”，遇到相同问题的不要太纠结。
