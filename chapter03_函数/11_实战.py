# -*- coding:utf-8 -*-
# @author Kuangjm
# @date 2021/12/13
# @file 11_实战.py

"""
Collatz 序列
编写一个名为 collatz()的函数，它有一个名为 number 的参数。
如果参数是偶数，那么 collatz()就打印出 number // 2，并返回该值。
如果 number 是奇数，collatz()就打印并返回 3 * number + 1。

然后编写一个程序，让用户输入一个整数，并不断对这个数调用 collatz()，直
到函数返回值１（令人惊奇的是，这个序列对于任何整数都有效，利用这个序列，
你迟早会得到 1！既使数学家也不能确定为什么。你的程序在研究所谓的“Collatz
序列”，它有时候被称为“最简单的、不可能的数学问题”）。

记得将 input()的返回值用 int()函数转成一个整数，否则它会是一个字符串。
"""


def collatz(number):
    if (number % 2 == 0):
        result = number // 2
    else:
        result = 3 * number + 1
    return result

while True:
    try:
        flag = int(input('请输入一个数：'))
        break
    except ValueError:
        print('Error,请输入一个整数')

while flag != 1:
    flag = collatz(flag)
    print(flag)
