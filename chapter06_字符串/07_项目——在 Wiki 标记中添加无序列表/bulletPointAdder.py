# -*- coding:utf-8 -*-
# @author Kuangjm
# @date 2022/1/7
# @file bulletPointAdder.py

"""
bulletPointAdder.py 脚本将从剪贴板中取得文本，在每一行开始处加上星号和空格，然后将这段新的文本贴回到剪贴板。例如，如果我将下面的文本复制到剪贴板
（取自于维基百科的文章“List of Lists of Lists”）：
Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars
然后运行 bulletPointAdder.py 程序，剪贴板中就会包含下面的内容：
* Lists of animals
* Lists of aquarium life
* Lists of biologists by author abbreviation
* Lists of cultivars
"""
import pyperclip
text = pyperclip.paste()

text_split = text.split("\n")

result = ""
for line in text_split:
    result += "* "+line+"\n"

pyperclip.copy(result)


