# -*- coding:utf-8 -*-
# @author Kuangjm
# @date 2021/12/13
# @file 01_def函数和返回值.py

import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

# 求值为 1 和 9 之间的一个随机整数（包括 1 和 9）
r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)

#默认返回None值
def sount():
    test = "test"
    t = 't'
    print(type(test))
    print(type(t))

test = sount()
print(test == None)