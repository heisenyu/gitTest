# -*- coding:utf-8 -*-
# @author Kuangjm
# @date 2021/12/13
# @file 04_print()函数.py

#print()函数有可选的变元 end 和 sep，分别指定在参数末尾打印什么，以及在参数之间打印什么来隔开它们。

# print()函数自动在传入的字符串末尾添加了"换行符"。但是，可以设置 end 关键字参数，将它变成另一个字符串
print('Hello', end='')
print('World')

#print()传入多个字符串值，该函数就会自动用一个 空格 分隔它们,可以传入 sep 关键字参数，替换掉默认的分隔字符串。
print('cats', 'dogs', 'mice')

print('cats', 'dogs', 'mice', sep=',')
