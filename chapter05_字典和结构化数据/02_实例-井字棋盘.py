# -*- coding:utf-8 -*-
# @author Kuangjm
# @date 2022/1/7
# @file 02_实例-井字棋盘.py

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

print(theBoard)

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
printBoard(theBoard)


# turn = 'X'
# for i in range(len(theBoard)):
#     print('Turn for ' + turn + '. Move on which space?')
#     move = input()
#     theBoard[move] = turn
#     if turn == 'X':
#         turn = 'O'
#     else:
#         turn = 'X'
#     printBoard(theBoard)


"""
嵌套的字典和列表
"""
allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
'Bob': {'ham sandwiches': 3, 'apples': 2},
'Carol': {'cups': 3, 'apple pies': 1}}
import pprint
count = {}
for value in allGuests.values():
    for k,v in value.items():
        print(k, v, sep='->')
        count.setdefault(k,0)
        count[k] += v
pprint.pprint(count)


