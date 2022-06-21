# -*- coding:utf-8 -*-
# @author Kuangjm
# @date 2021/12/10
# @file 03_for循环.py

'''
for 语句看起来像 for i in range(5):这样，总是包含以下部分：
 for 关键字；
 一个变量名；
 in 关键字；
 调用 range()方法，最多传入 3 个参数；
 冒号；
 从下一行开始，缩退的代码块（称为 for 子句）。
'''

# 前两个参数分别是起始值和终止值，第三个参数是“步长”(左闭右开
# )
for i in range(0, 10, 2):
    print(i)

for i in range(10, 0, -2):
    print(i)