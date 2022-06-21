# -*- coding:utf-8 -*-
# @author Kuangjm
# @date 2022/1/4
# @file 07_引用.py

import copy

"""
变量包含对列表值的引用，而不是列表值本身。但对于字符串和整数值，变量就包含了字符串或整数值。
在变量必须保存可变数据类型的值时，例如列表或字典(元素可以改变)，Python 就使用引用。
对于不可变的数据类型的值，例如字符串、整型或元组（元素不能改变），Python变量就保存值本身
"""

l1 = [1,2,3]
l2 = l1
l1.insert(0,0)
print(l2)

l1 = [1,2,3]
l2 = l1.copy()
l1.insert(0,0)
print(l2)

"""
嵌套list，需要使用深拷贝
"""

#浅拷贝
l1 = [1,[7,8,9],2,3]
l2 = l1.copy()
l1[1][0]='a'
print(l2)

#调用copy方法，浅拷贝
l1 = [1,[7,8,9],2,3]
l2 = copy.copy(l1)
l1[1][0]='a'
print(l2)

#调用copy方法，深拷贝
l1 = [1,[7,8,9],2,3]
l2 = copy.deepcopy(l1)
l1[1][0]='a'
print(l2)
