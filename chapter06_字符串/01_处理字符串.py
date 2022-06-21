# -*- coding:utf-8 -*-
# @author Kuangjm
# @date 2022/1/7
# @file 01_处理字符串.py

"""
单引号
"""
#'Say hi to Bob's mother.'

"""
字符串可以用 双引号 开始和结束，就像用单引号一样。
使用双引号的一个好处，就是字符串中可以使用单引号字符。
"""
print("That is Alice's cat.")

"""
转义字符
"""
print('Say hi to Bob\'s mother.')

"""
原始字符串
"""
print(r'That is Carol\'s cat.')

"""
用三重引号的多行字符串,常用于sql等有规范的字符串
"""
print('''Dear Alice,
Eve's cat has been arrested for catnapping,'' cat burgl""ary, and extortion.
Sincerely,
Bob''')

"""
#是单行注释
用三重引号的多行注释
"""
