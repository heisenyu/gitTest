# -*- coding:utf-8 -*-
# @author Kuangjm
# @date 2022/1/4
# @file 06_字符串和元组和列表.py

#字符串和列表实际上很相似，字符串是单个文本字符的列表。
# 对列表的许多操作，也可以作用于字符串：按下标取值、切片、用于 for 循环、用于 len()，以及用于 in 和 not in 操作符

name = 'Zophie'
"""
索引从0开始
左闭右开
"""
print(name[-1])
print(name[0:-1])
for i in range(len(name)):
    print(name[i])

"""
但列表和字符串在一个重要的方面是不同的。列表是“可变的”数据类型，它的值可以添加、删除或改变。但是，字符串是“不可变的”，它不能被更改。
"""
name = 'Zophie a cat'

#name[7] = 'the'


#“元组”数据类型几乎与列表数据类型一样。
"""
不同点 1、首先，元组输入时用圆括号()，而不是用方括号[]。2、元组像字符串一样，是不可变的。元组不能让它们的值被修改、添加或删除。
"""
eggs = ('hello', 42, 0.5)
lis = ['hello', 42, 0.5]

print(eggs[0])
print(lis[0])

eggs = ('hello', 42, 0.5)
#eggs[1] = 99

#如果元组中只有一个值，你可以在括号内该值的后面跟上一个逗号，表明这种情况
print(type(('hello',)))

print(type(('hello')))


"""
list()和 tuple()函数来转换类型
"""
lis = [1,2,3]
tup = ('a','b','c')
s = 'str'

print(tuple(lis))
print(tuple(s))
print(list(tup))
print(list(s))
print(str(lis))
print(str(tup))
