# -*- coding:utf-8 -*-
# @author Kuangjm
# @date 2022/1/10
# @file 06_字符分类.py

import re

"""
表示数字的几种方式
"""

str = 'My number is 415-555-4242.'
regex_num = r'\d'
regex_num1 = r'[^\D]'
regex_num2 = r'[0123456789]'
regex_num3 = r'[0-9]'
regex_num4 = r'0|1|2|3|4|5|6|7|8|9'

print(re.compile(regex_num).findall(str))
print(re.compile(regex_num1).findall(str))
print(re.compile(regex_num2).findall(str))
print(re.compile(regex_num3).findall(str))
print(re.compile(regex_num4).findall(str))

# TODO 插入字符和美元字符
"""
在正则表达式的开始处使用插入符号（^），表明匹配必须发生在被查找文本开始处。
类似地，可以再正则表达式的末尾加上美元符号（$），表示该字符串必须以这个正则表达式的模式结束。
"""

# 从开始到结束都是数字的字符串
wholeStringIsNum = re.compile(r'^\d+$')
print(wholeStringIsNum.search('1234567890').group())

# TODO 用点-星匹配所有字符
"""
点-星使用“贪心”模式：它总是匹配尽可能多的文本。要用“非贪心”模式匹配所有文本，就使用点-星和问号。
"""
str = "<To serve man> for dinner.>"
regex1 = r"<.*?>"
regex2 = r"<.*>"

print(re.compile(regex1).search(str).group())
print(re.compile(regex2).search(str).group())

# TODO 用句点字符匹配换行
"""
点-星将匹配除换行外的所有字符。
通过传入 re.DOTALL 作为 re.compile()的第二个参数，可以让句点字符匹配所有字符，包括换行字符。
"""
str = "('Serve the public trust.\nProtect the innocent.\nUphold the law."
regex = r".*"

print(re.compile(regex).search(str).group())
print(re.compile(regex, re.DOTALL).search(str).group())

# TODO 不区分大小写的匹配
"""
要让正则表达式
不区分大小写，可以向 re.compile()传入 re.IGNORECASE 或 re.I，作为第二个参数。
"""

str = 'Al, why does your programming book talk about rObOcoP so much?'
regex = r"robocop"
print(re.compile(regex, re.I).search(str).group())

# TODO 用 sub()方法替换字符串

"""
正则表达式不仅能找到文本模式，而且能够用新的文本替换掉这些模式。
Regex对象的 sub()方法需要传入两个参数。
第一个参数是一个字符串，用于取代发现的匹配。在 sub()的第一个参数中，可以输入\1、\2、\3……。表示“在替换中输入分组 1、2、3……的文本”。
第二个参数是一个字符串，即正则表达式。sub()方法返回替换完成后的字符串。
"""

str = 'Agent Alice gave the secret documents to Agent Bob.'
regex = r"Agent (\w)\w*"
print(re.compile(regex).sub(r'\1***', str))
# TODO 管理复杂的正则表达式
"""
但匹配复杂的文本模式，可能需要长的、费解的正则表达式。
你可以告诉 re.compile()，忽略正则表达式字符串中的空白符和注释，从而缓解这一点。
要实现这种详细模式，可以向 re.compile()传入变量 re.VERBOSE，作为第二个参数。
"""
phoneRegex = re.compile(r'''(
      (\d{3}|\(\d{3}\))? # area code
      (\s|-|\.)? # separator
      \d{3} # first 3 digits
      (\s|-|\.) # separator
      \d{4} # last 4 digits
      (\s*(ext|x|ext.)\s*\d{2,5})? # extension
)''', re.VERBOSE)

#如果希望正则表达式不区分大小写，并且句点字符匹配换行，并希望使用 re.VERBOSE 来编写注释，可以使用管道字符（|）将变量组合起来
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)


