# -*- coding:utf-8 -*-
# @author Kuangjm
# @date 2022/1/10
# @file 12_项目——电话号码和 E-mail 地址提取程序.py

"""
假设你有一个无聊的任务，要在一篇长的网页或文章中，找出所有电话号码和邮件地址。
如果手动翻页，可能需要查找很长时间。
如果有一个程序，可以在剪贴板的文本中查找电话号码和 E-mail 地址，那你就只要按一下 Ctrl-A 选择所有文本，
按下 Ctrl-C 将它复制到剪贴板，然后运行你的程序。它会用找到的电话号码和 E-mail地址，替换掉剪贴板中的文本。


作为一个例子，打开你的 Web 浏览器，访问 No Starch Press 的联系页面
http://www.nostarch.com/contactus.htm。按下 Ctrl-A 选择该页的所有文本，按下 Ctrl-C
将它复制到剪贴板。运行这个程序，输出看起来像这样：
Copied to clipboard:
800-420-7240
Python 编程快速上手——让繁琐工作自动化
415-863-9900
415-863-9950
info@nostarch.com
media@nostarch.com
academic@nostarch.com
help@nostarch.com

"""
import re

import pyperclip

phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?              # area code
(\s|-|\.)?                      # separator
(\d{3})                         # first 3 digits
(\s|-|\.)                       # separator
(\d{4})                         # last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
)''', re.VERBOSE)

emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+   # username
@                   # @ symbol
[a-zA-Z0-9.-]+      # domain name
(\.[a-zA-Z]{2,4})   # dot-something
)''', re.VERBOSE)

text = str(pyperclip.paste())

matches = []

for groups in phoneRegex.findall(text):
    print(groups) #groups是元组
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if  groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    print(groups)
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')



