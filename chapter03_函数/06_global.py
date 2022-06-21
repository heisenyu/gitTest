# -*- coding:utf-8 -*-
# @author Kuangjm
# @date 2021/12/13
# @file 06_global.py

"""
有 4 条法则，来区分一个变量是处于局部作用域还是全局作用域：
1．如果变量在全局作用域中使用（即在所有函数之外），它就总是全局变量。
2．如果在一个函数中，有针对该变量的 global 语句，它就是全局变量。
3．否则，如果该变量用于函数中的赋值语句，它就是局部变量。
4．但是，如果该变量没有用在赋值语句中，它就是全局变量。

"""

eggs = 'global'


def spam():
    # eggs = 'test' 报错
    global eggs
    eggs = 'spam' # this is the global


def bacon():
    eggs = 'bacon'  # this is a local


def ham():
    print(eggs)  # this is the global


eggs = 42  # this is the global
spam()
bacon()
print(eggs) #spam
