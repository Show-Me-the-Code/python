# coding = utf-8

from tools import imager
from PIL import ImageFont


# 第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字
def add_num(image_path):
    im = imager.open_image(image_path)
    if im is not None:
        font = ImageFont.truetype('Arial.ttf', 20)
        w, h = im.size
        point = (w - 10, 0)
        imager.draw_text(im, "8", point, font)
        im.show()


# 第 0001 题：使用 Python 生成 200 个激活码（或者优惠券）
import uuid

def create_activation_code(num=200):
    codes = []
    for i in range(num):
        code = str(uuid.uuid1())
        code = code.replace('-', '')
        codes.append(code)

    return codes


# 第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
import pymysql

def save_activation_code_to_mysql():
    conn = pymysql.connect(host='localhost', user='root', charset='UTF8')
    cur = conn.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS code_mysql")
    cur.execute("USE code_mysql")
    cur.execute("CREATE TABLE IF NOT EXISTS codes (id INT, code VARCHAR(255))")

    codes = create_activation_code(200)
    for code in codes:
        cur.execute("INSERT INTO codes (code) values(%s)", [code])

    conn.commit()

    cur.execute("SELETE * FROM codes")
    data = cur.fetchall()
    print("data:%s" % data)

    cur.close()
    conn.close()


# 第 0003 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。
import redis

def save_activation_code_to_redis():
    re = redis.Redis(host='127.0.0.1', port=6379, db=0)

    codes = create_activation_code(200)
    for code in codes:
        re.lpop('codes', code)

    print("data:%s" % re.get('codes'))


# 第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数。
import re

def number_of_words(file_path=None):
    num = 0

    if file_path is None:
        return num

    file = open(file_path, 'r')
    content = file.read()
    content = " " + content
    pattern = re.compile(u'\s+\w+')
    match = pattern.findall(content)
    num = len(match)

    return num


# 第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
def reset_images_size(dir_path=None):
    if dir_path is None:
        return

    for root, dirs, files in os.walk(dir_path):
        for path in files:
            if path.startswith("."):
                continue

            file_path = os.path.join(root, path)
            image = imager.open_image(file_path)
            if image is not None:
                new_image = imager.reset_image_size(image, 640, 1136)
                imager.save(new_image, file_path)


# 第 0006 题：你有一个目录，放了你一个月的日记，都是 txt，
# 为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
# 思路:哪个词出现的最多,哪个词就是最重要的词
import operator

def get_most_important_word(dir_path=None):
    if dir_path is None:
        return None

    for root, dirs, files in os.walk(dir_path):
        for path in files:
            if not path.endswith("txt"):
                continue

            file_path = os.path.join(root, path)
            content = open(file_path, 'r').read().lower()

            words = content.split()
            word_dic = {}
            for word in words:
                if word in word_dic.keys():
                    word_dic[word] += 1
                else:
                    word_dic[word] = 1

            if len(word_dic):
                word_list = sorted(word_dic.items(), key=lambda x:x[1], reverse=True)
                print("%s : %s -- %d" % (path, word_list[0][0], word_list[0][1]))



# 第 0007 题：有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来
import os

# 注释://, #, /* */, """ """, ''' '''
def lines_of_codes(dir_path=None):
    code_num = 0
    note_num = 0
    blank_line_num = 0
    if dir_path is None:
        return code_num, note_num, blank_line_num

    for root, dirs, files in os.walk(dir_path):
        mut_note = None
        for path in files:
            if path.startswith("."):
                continue

            file_path = os.path.join(root, path)
            for count, line in enumerate(open(file_path, "rU")):

                # 判断是否是空行
                if not line.split():
                    blank_line_num += 1
                    continue

                # 判断是否多行注释
                if mut_note is not None:
                    note_num += 1
                    match_note = re.match("\*/|\"\"\"|\'\'\'", line)
                    if match_note is not None:
                        mut_note = None
                        match_note = re.match("\/\*|\"\"\"|\'\'\'", line)
                        if match_note is not None:
                            mut_note = line[match_note.pos:(match_note.endpos - 1)]

                    continue
                else:
                    match_note = re.match("\/\*|\"\"\"|\'\'\'", line)
                    if match_note is not None:
                        note_num += 1
                        mut_note = line[match_note.pos:(match_note.endpos - 1)]
                        continue

                # 判断单行注释
                match_note1 = re.match("\s*(#|//).*\n*", line)
                if match_note1 is not None:
                    note_num += 1
                    continue

                pass

            code_num += count + 1

    return code_num, note_num, blank_line_num

# 第 0008 题：一个HTML文件，找出里面的正文
# 使用 pip install beautifulsoup4
from bs4 import BeautifulSoup

def get_html_context(url=None):
    if url is None:
        return None

    content = request.urlopen(url).read().decode("utf-8")
    soup = BeautifulSoup(content)
    [script.extract() for script in soup.find_all('script')]
    [style.extract() for style in soup.find_all('style')]

    soup.prettify()
    reg = re.compile("<[^>]*>")
    ret_content = reg.sub('', soup.prettify())
    # print(ret_content)

    return ret_content


# 第 0009 题：一个HTML文件，找出里面的链接
# 查找<a>, 用 HTMLParser
from urllib import request
from tools import dxhtmlparser

def get_html_links(url=None):
    if url is None:
        return None

    content = request.urlopen(url).read().decode("utf-8")
    dxparser = dxhtmlparser.DXHTMLParser('a', 'href', url)
    dxparser.feed(content)

    links = dxparser.getrets()

    return links

# 第 0010 题：使用 Python 生成字母验证码图片
def create_verification_code():
    im, str = imager.verification_code()
    im.show()


# 第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，
# 北京, 程序员, 公务员, 领导, 牛比, 牛逼, 你娘, 你妈, love, sex, jiangge
# 当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

def find_sensitive_words(sensitive_file=None, input_string=None):
    if sensitive_file is None or input_string is None:
        return None

    file = open(sensitive_file, "r")
    sensitive_words = file.read().split()

    is_sensitive = False
    for sensitive in sensitive_words:
        if sensitive in input_string:
            is_sensitive = True
            print("Freedom")

    if not is_sensitive:
        print("Human Rights")


# 第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，
# 当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。

def replace_sensitive_words(sensitive_file=None, input_string=None):
    if sensitive_file is None or input_string is None:
        return None

    file = open(sensitive_file, "r")
    sensitive_words = file.read().split()

    for sensitive in sensitive_words:
        if sensitive in input_string:
            replace_str = "*" * len(sensitive)
            input_string = input_string.replace(sensitive, replace_str)

    print(input_string)

# 第 0013 题： 用 Python 写一个爬图片的程序
from tools import geturlimgs

def get_url_imgs(url=None):
    if url is None:
        return None

    tmp = geturlimgs.geturlimgs()
    tmp.get_imgs(url, "/Users/xieyajie/Desktop/Python/ShowMeCode/xyjxyf/0013/")



# 第 0014 题： 纯文本文件 student.txt为学生信息, 写到 student.xls 文件中
# 第 0015 题： 纯文本文件 city.txt为城市信息,写到 city.xls 文件中
import json
import xlwt

def dictxt_to_xls(file_path=None):
    if file_path is None:
        return

    file = open(file_path, 'r')
    if file is None:
        return

    content = json.loads(file.read())
    list_data = sorted(content.items(), key=lambda d:d[0])

    (path, name)=os.path.split(file.name)
    file_name = name.split('.')[0]

    wb = xlwt.Workbook()
    ws = wb.add_sheet(file_name)

    row = 0
    for item in list_data:
        col = 0
        ws.write(row, col, item[0])
        col += 1

        value = item[1]
        if type(value) == list:
            for obj in value:
                ws.write(row, col, obj)
                col += 1
        else:
             ws.write(row, col, value)
        row += 1

    save_path = path + "/" + file_name + ".xls"
    wb.save(save_path)


# 第 0016 题： 纯文本文件 numbers.txt, 请将上述内容写到 numbers.xls 文件中
def listtxt_to_xls(file_path=None):
    if file_path is None:
        return

    file = open(file_path)
    if file is None:
        return

    content = json.loads(file.read())
    content.sort(key=lambda x:x[0])

    (path, name)=os.path.split(file.name)
    file_name = name.split('.')[0]
    wb = xlwt.Workbook()
    ws = wb.add_sheet(file_name)

    for i in range(len(content)):
        col = 0
        list = content[i]
        for value in list:
            ws.write(i, col, content[i][col])
            col += 1

    save_path = path + "/" + file_name + ".xls"
    wb.save(save_path)

# pip3 install xlrd
import xlrd
def read_xls(file_path=None):
    if file_path is None:
        return None

    data_list = {}
    wb = xlrd.open_workbook(file_path)
    sheet_names = wb.sheet_names()
    for name in sheet_names:
        table = wb.sheet_by_name(name)
        table_data = []
        for i in range(table.nrows):
            row_data = table.row_values(i)
            table_data.append(row_data)

        data_list[name] = table_data

    return data_list


# 第 0017 题： 将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中
# 使用DOM
from tools import stringer
from xml.dom.minidom import Document

def write_student_to_xml(dic=None, to_path=None):
    if dic is None or to_path is None:
        return None

    doc = Document()
    root_node = doc.createElement("root")
    doc.appendChild(root_node)

    stu_node = doc.createElement("students")
    root_node.appendChild(stu_node)

    note_node = doc.createComment("\n\t学生信息表\n\t\"id\" : [名字, 数学, 语文, 英文]\n\t")
    stu_node.appendChild(note_node)

    # data = json.dumps(dic, ensure_ascii=False, indent=1)
    dic_node = doc.createTextNode(stringer.dict_to_json(dic, "\t\t"))
    stu_node.appendChild(dic_node)

    file = open(to_path, "w")
    file.write(doc.toprettyxml())
    # doc.writexml(file,'    ','    ','\n','utf-8')
    file.close()

# 第 0018 题： 将 第 0015 题中的 city.xls 文件中的内容写到 city.xml 文件中
# 使用lxml
import codecs
from lxml import etree

def write_city_to_xml(dic=None, to_path=None):
    if dic is None or to_path is None:
        return None

    root_node = etree.Element('root')
    root_node.text = "\n\t"

    city_node = etree.SubElement(root_node, 'citys')

    comment_node = etree.Comment("\n城市信息\n")
    comment_node.tail = "\n\t"
    city_node.append(comment_node)

    city_node.text = "\n\t" + stringer.dict_to_json(dic, "\t") + u'\n'
    city_node.tail = "\n"

    city_tree = etree.ElementTree(root_node)
    city_tree.write(to_path, pretty_print=True, xml_declaration=True, encoding='utf-8')
    # output = codecs.open(to_path, 'w', 'utf-8')
    # output.write(etree.tounicode(city_tree.getroot()))
    # output.close()


# 第 0019 题： 将 第 0016 题中的 numbers.xls 文件中的内容写到 numbers.xml 文件中
def write_numbers_to_xml(list=None, to_path=None):
     if list is None or to_path is None:
        return None

     root_node = etree.Element('root')
     root_node.text = "\n\t"

     number_node = etree.SubElement(root_node, 'numbers')

     comment_node = etree.Comment("\n数字信息\n")
     comment_node.tail = "\n\t"
     number_node.append(comment_node)

     number_node.text = "\n\t" + stringer.list_to_json(list, "\t") + u'\n'
     number_node.tail = "\n"

     number_tree = etree.ElementTree(root_node)
     number_tree.write(to_path, pretty_print=True, xml_declaration=True, encoding='utf-8')


# 第 0020 题： 登陆中国联通网上营业厅 后选择「自助服务」 --> 「详单查询」，然后选择你要查询的时间段，点击「查询」按钮，
# 查询结果页面的最下方，点击「导出」，就会生成类似于 2014年10月01日～2014年10月31日通话详单.xls 文件。
# 写代码，对每月通话时间做个统计

import datetime

def statistics_month_time():
    dic = {}
    wb = xlrd.open_workbook("./0020/0020.xls")
    sheet = wb.sheets()[0]
    row_count = sheet.nrows

    for i in range(1, sheet.nrows):
        values = sheet.row_values(i)
        ym_str = values[2][:6]

        time_str = values[3]
        if '时' in time_str:
            time_str = re.sub('时', '.', time_str)
        if '分' in time_str:
            time_str = re.sub('分', '.', time_str)
        if '秒' in time_str:
            time_str = re.sub('秒', '', time_str)

        tmp = time_str.split('.')
        j = len(tmp) - 1
        sum = int(tmp[j])
        while j > -1:
            sum = sum + (len(tmp) - 1 - j) * 60 * int(tmp[j])
            j = j - 1

        if ym_str in dic:
            dic[ym_str] = dic[ym_str] + int(sum)
        else:
            dic[ym_str] = int(sum)

        # i = i + 1

    return dic


# 第 0021 题： 请使用 Python 对密码加密
from hashlib import sha256
from hmac import HMAC

def encrypt_password(password, salt=None):
    if salt is None:
        salt = os.urandom(8)

    if isinstance(password, str):
        password = password.encode('UTF-8')

    ret = password
    for i in range(10):
        ret = HMAC(ret, salt, sha256).digest()

    return salt + ret


# 第 0022 题： iPhone 6、iPhone 6 Plus 早已上市开卖。请查看你写得 第 0005 题的代码是否可以复用


# 第 0023 题： 使用 Python 的 Web 框架，做一个 Web 版本 留言簿 应用


# 第 0024 题： 使用 Python 的 Web 框架，做一个 Web 版本 TodoList 应用


# 第 0025 题： 使用 Python 实现：对着电脑吼一声,自动打开浏览器中的默认网站
# 在文件夹0025中实现


if __name__ == "__main__":
    # 0000
    # add_num(".0000/0000.jpg")

    # 0001
    # create_activation_code()

    # 0002 ?????
    # save_activation_code_to_mysql()

    # 0003
    # save_activation_code_to_redis()

    # 0004
    # number_of_words("./0004/0004.txt")

    # 0005
    # reset_images_size("./0005")

    # 0006
    # get_most_important_word("./0006")

    # 0007
    # code, note, blank_line = lines_of_codes("./0007")
    # print("代码行数:%i\n注释行数:%i\n空行行数:%i" % (code, note, blank_line))

    # 0008
    # get_html_context("http://blog.bccn.net")

    # 0009
    # get_html_links("http://blog.bccn.net")

    # 0010
    # create_verification_code()

    # 0011
    # find_sensitive_words("./0011/0011.txt", "haha, 北京不错")

    # 0012
    # replace_sensitive_words("./0011/0011.txt", "haha, 北京不错")

    # 0013
    # get_url_imgs("http://www.ivsky.com/tupian/beijing_t1542/index_2.html")

    # 0014
    # dictxt_to_xls("./0014/student.txt")

    # 0015
    # dictxt_to_xls("./0015/city.txt")

    # 0016
    # listtxt_to_xls("./0016/numbers.txt")

    # 0017
    # student_dic = read_xls("./0017/student.xls")
    # for key in student_dic:
    #     student = student_dic[key]
    #
    #     dic = {}
    #     for list in student:
    #         dic[list[0]] = list[1:]
    #
    #     write_student_to_xml(dic, "./0017/student.xml")
    #
    #     break


    # 0018
    # city_dic = read_xls("./0018/city.xls")
    # for key in city_dic:
    #     city = city_dic[key]
    #
    #     dic = {}
    #     for list in city:
    #         dic[list[0]] = list[1:]
    #
    #     write_city_to_xml(dic, "./0018/city.xml")
    #
    #     break
    
    # 0019
    # number_dic = read_xls("./0019/numbers.xls")
    # for key in number_dic:
    #     number = number_dic[key]
    #     write_numbers_to_xml(number, "./0019/numbers.xml")
    #
    #     break

    # 0020
    # statistics_month_time()

    # 0021
    encrypt_password("123")

    # 0022

    # 0023

    # 0024

    # 0025
