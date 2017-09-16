#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
* 0016
* by ahwz001
* 2017/9/11
* Thanks for this project. I learned a lot here.
"""

import xlwt
 

def deal_text(source_file):
    """convert txt file to a list of  data list.
    return the list.
    """
    with open(source_file) as fn:
        content = fn.read()
    data = eval(content)
    return data


def save_to_xls(data, des_file):
    """write a list of list to xls file.
    data: list of list of data.
    """
    wb = xlwt.Workbook(encoding = 'utf-8')
    sheet = wb.add_sheet('numbers',cell_overwrite_ok=True)
    row, column = 0,0

    for  numbers in data:    
        for num in numbers:
            sheet.write(row, column, num)   
            column += 1     
            print "write ... ", num,
        row += 1
        column = 0
        print '\n'
    print 'ALL DONE!'

    wb.save(des_file)


def main():
    source_file = 'numbers.txt'
    des_file = 'numbers.xls'
    data = deal_text(source_file)
    save_to_xls(data, des_file)


if __name__ == '__main__':
    main()
