# -*- coding:utf-8 -*-
# @author Kuangjm
# @date 2021/12/13
# @file 07_异常.py

#42/0

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))  #None
print(spam(1))


def spam(divideBy):
    return 42 / divideBy
try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))  #print(spam(1))从未被执行是因为，一旦执行跳到 except 子句的代码，就不会回到 try 子句。
except ZeroDivisionError:
    print('Error: Invalid argument.')



