# -*- coding:utf-8 -*-
# @author Kuangjm
# @date 2022/1/10
# @file 02_更多模式.py
import re

#TODO 1、利用括号分组

str = 'My number is 415-555-4242.'

regex_num = r'(\d\d\d)-(\d\d\d-\d\d\d\d)'
pattern_num = re.compile(regex_num)
match_num = pattern_num.search(str)

"""
正则表达式字符串中的第一对括号是第 1 组。第二对括号是第 2 组。
向 group()匹配对象方法传入整数 1 或 2，就可以取得匹配文本的不同部分。
向 group()方法传入 0 或不传入参数，将返回整个匹配的文本。
"""
print(match_num.group())
print(match_num.group(0))
print(match_num.group(1))
print(match_num.group(2))
print(match_num.groups())

"""
因为 mo.groups()返回多个值的元组，所以你可以使用多重赋值的技巧，每个值赋给一个独立的变量
"""

pre,last = match_num.groups()
print(pre)
print(last)


#TODO 2、用 管道 匹配多个分组
"""
字符|称为“管道”。希望匹配许多表达式中的一个时，就可以使用它。
"""
print(re.compile(r'Bat(man|mobile|copter|bat)').search('Batmobile lost a wheel').group(0))


#TODO 3、用 问号 实现可选匹配（0次或一次）
str = 'My number is 415-555-4242.'
str2 = 'My number is 555-4242.'

regex_num = r'(\d\d\d-)?(\d\d\d-\d\d\d\d)'
pattern_num = re.compile(regex_num)
match_num = pattern_num.search(str)
match_num2 = pattern_num.search(str2)
print(match_num.group())
print(match_num2.group())

#TODO 4、用 星号 匹配零次或多次
str = 'My number is 415-555-4242.'

regex_num = r'\d*-\d*-\d*'
pattern_num = re.compile(regex_num)
match_num = pattern_num.search(str)

print(match_num.group())

#TODO 5、用 加号 匹配一次或多次
str = 'My number is 415-555-4242.'

regex_num = r'\d+-\d+-\d+'
pattern_num = re.compile(regex_num)
match_num = pattern_num.search(str)

print(match_num.group())

#TODO 6、用 花括号 匹配特定次数
str = 'My number is 415-555-4242.'

regex_num = r'\d{3,4}'
pattern_num = re.compile(regex_num)
match_num = pattern_num.search(str)

print(match_num.group())

print("====================================")
str = 'My number is 415-555-4242.'

regex_num = r'\d{3,4}'
pattern_num = re.compile(regex_num)
match_num = pattern_num.findall(str) #findall返回类型list
print(match_num)

#TODO 7、贪心和非贪心匹配
"""
Python 的正则表达式默认是“贪心”的，这表示在有二义的情况下，它们会尽可能匹配最长的字符串。
"""

str = 'My number is 415-555-4242.'

regex_num = r'\d{3,4}?'
pattern_num = re.compile(regex_num)
match_num = pattern_num.findall(str) #findall返回类型list
print(match_num)


"""
search()将返回一个Match对象，包含被查找字符串中的“第一次”匹配的文本，
而 findall()方法将返回一组字符串，包含被查找字符串中的所有匹配。
如果在正则表达式中有分组，那么 findall 将返回元组的列表。
"""
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))


