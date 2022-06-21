# -*- coding:utf-8 -*-
# @author Kuangjm
# @date 2021/12/31
# @file 01_列表的增删查改.py

a = ['1',2,3]

print(a[0],'b')

print(a[0]+'b')

#增
print(a+['a','b'])

l = [1,2,3]
l.append(4)
l.insert(0,0)
print(l)

#删
del a[0]
print(a)

#如果该值在列表中出现多次，只有第一次出现的值会被删除。
#不能按照索引来删除
l = ['a','b','c']
l.remove('a')
print(l)

#查
a[0]
"""
索引从0开始
左闭右开
"""
print(a)
print(a[:])
print(a[-1])
print(a[0:2])

l = ['a','b','c','a']
print('=========')
print(l.index('a'))
print(l.count('a'))

#改
a[-1]=0
print(a)
"""
批量修改
"""
a[0:-1] = [1,2,3]
print(a)

#复制地址
a = [1,2,3]
b = a
a[0] = 'a'
print(b)
b[-1] = 'c'
print(a)

#新的列表
a = [1,2,3]
b = a.copy()
a[0] = 'a'
print(b)
b[-1] = 'c'
print(a)