#! usr/bin/python3
"""
第 0008 题：一个HTML文件，找出里面的正文。
"""

import re, urllib.request, time
url = input('Enter the URL which you wish to extract > ')
if '' == url:
    url = "https://adblockplus.org/zh_CN/acceptable-ads"

print('We will extract text data from ' + url + ' :')


with urllib.request.urlopen(url) as response:
    content = response.read()
    try:
        content = content.decode('utf-8')
    except UnicodeDecodeError:
        content = content.decode('gbk')
    #remove some special content
    content = re.sub(r'<title.+?</title>', '', content, flags = re.DOTALL)
    content = re.sub(r'<head(er)?.+?</head(er)?>', '',
                     content, flags = re.DOTALL)
    content = re.sub(r'<(no)?script.+?</(no)?script>', '',
                     content, flags = re.DOTALL)
    content = re.sub(r'<style.+?</style>', '', content, flags = re.DOTALL)
    content = re.sub(r'<form.+?</form>', '', content, flags = re.DOTALL)
    content = re.sub(r'<footer.+?</footer>', '', content, flags = re.DOTALL)
    #find text and fill them in a list
    result = re.findall(r'(?<=>)[^><]+?(?=<)', content)
    text = ''.join(result).strip()
    file_name = time.strftime('%Y%m%d%H%M%S') + '.txt'
    with open(file_name, 'wt') as textfile:
        #textfile.write(text)
        print(text, file = textfile)
    print('Extract finished, the text file is: ' + file_name)

        
