# -*- coding:utf-8 -*-
# @author Kuangjm
# @date 2022/1/7
# @file 02_常用方法.py

# upper()、lower()、isupper()和 islower()
"""
upper()和 lower()字符串方法返回一个新字符串，其中原字符串的所有字母都被
相应地转换为大写或小写。字符串中非字母字符保持不变。

如果字符串至少有一个字母，并且 所有 字母都是大写或小写，isupper()和
islower()方法就会相应地返回布尔值 True。
"""

s = 'a1b2C3'

print(s.upper())
print(s.lower())

print(s)

print(s.isupper())
print(s.islower())

print(s.upper().isupper())
print(s.lower().islower())


"""
isalpha()返回 True，如果字符串只包含字母，并且非空；
isalnum()返回 True，如果字符串只包含字母和数字，并且非空；
isdecimal()返回 True，如果字符串只包含数字字符，并且非空；
isspace()返回 True，如果字符串只包含空格、制表符和换行，并且非空；
istitle()返回 True，如果字符串仅包含以大写字母开头、后面都是小写字母的单词。
"""

print("""
startswith()和 endswith()
""")
"""
startswith()和 endswith()方法返回 True，如果它们所调用的字符串以该方法传入的字符串开始或结束。
"""

print('Hello world!'.startswith('He'))
print('Hello world!'.endswith('ld!'))

print("""
join()和 split()
""")

"""
join()方法在一个字符串上调用，参数是一个字符串 列表 ，返回一个字符串。返回的字符串由传入的列表中每个字符串连接而成。
"""
strList = ['cats', 'rats', 'bats']
print('~'.join(strList))

print("cats~rats~bats".split("~"))

print("""
rjust()、ljust()和 center()方法对齐文本
""")

"""
利用 rjust()、ljust()和 center()让你确保字符串整齐对齐，即使你不清楚字符串
有多少字符。
"""

"""
rjust()和 ljust()字符串方法返回调用它们的字符串的填充版本，通过插入空格来对齐文本。
这两个方法的第一个参数是一个整数长度，用于对齐字符串。第二个可选参数将指定一个填充字符，取代空格字符。
"""
print('Hello'.rjust(10))
print('Hello'.ljust(10))

print(len('Hello'.rjust(10)))
print(len('Hello'.ljust(10)))

print('Hello'.rjust(10,"*"))
print('Hello'.ljust(10,"~"))

"center()字符串方法与 ljust()与 rjust()类似，但它让文本居中"
print('Hello'.center(10))
print(len('Hello'.center(10)))
print('Hello'.center(10,"="))

print('center'.center(20,"="))
print("left".ljust(10,".")+"right".rjust(10,"."))

print("""
strip()、rstrip()和 lstrip()删除空白字符
""")

"""
strip()字符串方法将返回一个新的字符串，它的开头或末尾都没有空白字符。
lstrip()和 rstrip()方法将相应删除左边或右边的空白字符。
"""
spam = '   Hello  World   '
print(spam.strip())
print(spam.lstrip())
print(spam.rstrip())

print("""
pyperclip 模块拷贝粘贴字符串
""")

"""
pyperclip 模块有 copy()和 paste()函数，可以向计算机的剪贴板发送文本，或从它接收文本。
"""

import pyperclip

pyperclip.copy('Hello world!')
print(pyperclip.paste())


