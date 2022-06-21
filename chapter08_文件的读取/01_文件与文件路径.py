# -*- coding:utf-8 -*-
# @author Kuangjm
# @date 2022/1/10
# @file 01_文件与文件路径.py

import os
from pathlib import Path

"""
在Windows操作系统上，路径书写使用 倒斜杠 '\' 作为文件夹之间的分隔符。
但在macOS和Linux操作系统上，使用 正斜杠 '/' 作为它们的路径分隔符。
"""

print(Path('spam', 'bacon', 'eggs'))
print(str(Path('spam', 'bacon', 'eggs')))

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(Path(r'C:\Users\Al', filename))
