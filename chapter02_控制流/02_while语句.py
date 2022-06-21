# -*- coding:utf-8 -*-
# @author Kuangjm
# @date 2021/12/10
# @file 02_while语句.py

'''
while 语句总是包含下面几部分：
 关键字；
 条件（求值为 True 或 False 的表达式）；
 冒号；
 从新行开始，缩进的代码块（称为 while 子句）。
'''

name =''
while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')
