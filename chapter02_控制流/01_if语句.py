# -*- coding:utf-8 -*-
# @author Kuangjm
# @date 2021/12/10
# @file 01_if语句.py

# if 语句包含以下部分：
#  if 关键字；
#  条件（即求值为 True 或 False 的表达式）；
#  冒号；
#  在下一行开始，缩进的代码块（称为 if 子句）。

"""
if 语句包含以下部分：
 if 关键字；
 条件（即求值为 True 或 False 的表达式）；
 冒号；
 在下一行开始，缩进的代码块（称为 if 子句）。
"""

# 用于条件时，0、0.0 和''（空字符串）被认为是 False，其他值被认为是 True。

flag = 0
flag1 = 0.0
flag2 = ''
print(bool(flag))
print(bool(flag1))
print(bool(flag2))


name = input('请输入姓名：')
age = int(input('请输入年龄：'))
if name == 'Alice':
    print('Hi,' + name)
elif age > 10:
    print('')
else:
    print('not alice')
