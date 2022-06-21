# -*- coding:utf-8 -*-
# @author Kuangjm
# @date 2021/12/31
# @file 02_列表的使用.py


"""
for 循环的实质
"""
for i in range(4):
    print(i)

for i in [0,1,2,3]:
    print(i)

"""
列表的循环
"""
l = ['a','b','c','d']

for i in range(len(l)):
    print(i,l[i])


"""
重复变量赋值
"""
# names = []
#
# while True:
#     name = input('输入名字:')
#     if name == '':
#         break
#     names = names + [name]
#
# for name in names:
#     print(name+' ')

"""
in 和 not in 操作符
"""
print('a' in ['a', 'b', 'c'])


"""
多重赋值技巧
"""
l=['a', 'b', 'c']
a,b,c = l
print(a,b,c)