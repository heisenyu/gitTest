# -*- coding:utf-8 -*-
# @author Kuangjm
# @date 2021/12/13
# @file 05_函数作用域.py

eggs = 'global'

def spam():
    eggs = 'spam local'
    print(eggs)  # prints 'spam local'

def bacon():
    eggs = 'bacon local'
    print(eggs)  # prints 'bacon local'
    spam()
    print(eggs)  # prints 'bacon local'

bacon()
print(eggs)  # prints 'global'
