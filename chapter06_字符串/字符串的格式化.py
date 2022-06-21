# -*- coding:utf-8 -*-
# @author Kuangjm
# @date 2022/1/10
# @file 字符串的格式化.py

#format 格式化函数

"""
格式化字符串的函数 str.format()，它增强了字符串格式化的功能。

基本语法是通过 {} 和 : 来代替以前的 %
"""

print ("My name is %s and weight is %d kg!" % ('Zara', 21))

print ("My name is {} and weight is {} kg!")

print ("My name is {} and weight is {} kg!".format('Zara',21))

print ("{} 对应的位置是 {{0}}".format("runoob"))

print ("{{}} 对应的位置是 {0}".format("runoob"))

# 不设置指定位置，按默认顺序
s1 = "{} {}".format("hello", "world")

# 设置指定位置
s2 = "{0} {1}".format("hello", "world")

# 设置指定位置
s3 = "{1} {0} {1}".format("hello", "world")

print(s1,s2,s3,sep="\n")

#也可以设置参数：
print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))

# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com","tmp": "tmp"}
print("网站名：{name}, 地址 {url}".format(**site))

# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的

print("{:.2f}".format(3.1415926))
print("{:.0f}".format(3.1415926))
print("{:+.2f}".format(3.1415926))
print("{:+.2f}".format(-3.1415926))
print("{:.2%}".format(0.256))

