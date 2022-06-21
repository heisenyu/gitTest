# -*- coding:utf-8 -*-
# @author Kuangjm
# @date 2022/1/10
# @file 01_创建正则对象.py

import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())


str = 'My number is 415-555-4242.'
regex_num = r'\d\d\d-\d\d\d-\d\d\d\d'
pattern_num = re.compile(regex_num)
match_num = pattern_num.search(str)

if match_num != None:
    print(match_num.group())
