# -*- coding:utf-8 -*-
# @author Kuangjm
# @date 2022/1/4
# @file 04_sort方法.py

#reverse 关键字参数为 True，让 sort()按逆序排序。
spam = [2, 5, 3.14, 1, -7]
spam.sort()
print(spam)

spam = [2, 5, 3.14, 1, -7]
spam.sort(reverse=True)
print(spam)

#注意 TypeError 错误,不能对既有数字又有字符串值的列表排序
spam = [1, 3, 2, 4, 'Alice', 'Bob']

#sort()方法对字符串排序时，使用“ASCII 字符顺序”，而不是实际的字典顺序。
#如果需要按照普通的字典顺序来排序，就在 sort()方法调用时，将关键字参数key 设置为 str.lower。
spam = ['a', 'z', 'A', 'Z']
spam.sort()
print(spam)

spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)
print(spam)

