# -*- coding:utf-8 -*-
# @author Kuangjm
# @date 2022/1/10
# @file 18_实战.py

"""
强口令检测
写一个函数，它使用正则表达式，确保传入的口令字符串是强口令。
强口令的定义是：
长度不少于 8 个字符，
同时包含大写和小写字符，
至少有一位数字。
你可能需要用多个正则表达式来测试该字符串，以保证它的强度。
"""
import re


def isStrong(str):
    regex_len = r'\w{8,}'
    regex_low = r'\w*[a-z]\w*'
    regex_up = r'\w*[A-Z]\w*'
    regex_num = r'\w*[0-9]\w*'

    match_len = re.compile(regex_len).search(str)
    match_low = re.compile(regex_low).search(str)
    match_up = re.compile(regex_up).search(str)
    match_num = re.compile(regex_num).search(str)

    if (match_len==None):
        print("长度不少于 8 个字符")
        return False
    elif (match_low == None):
        print("至少有一位小写字母")
        return False
    elif (match_up == None):
        print("至少有一位大写字母")
        return False
    elif (match_num == None):
        print("至少有一位数字")
        return False
    else:
        print("是强口令")
        return True

str = ''
isStrong(str)



"""
strip()的正则表达式版本
写一个函数，它接受一个字符串，做的事情和 strip()字符串方法一样。
如果只传入了要去除的字符串，没有其他参数，那么就从该字符串首尾去除空白字符。
否则，函数第二个参数指定的字符将从该字符串中去除
"""
def strip(str , replace = ''):
    regex_blank = r'(^\s*)|(\s*$)'
    print(re.compile(replace).sub('', re.compile(regex_blank).sub('', str)))

str = '  asdas  asdas  asd tmo  '
strip(str)

