# -*- coding:utf-8 -*-
# @author Kuangjm
# @date 2022/1/4
# @file 10_实战.py

"""
假定有下面这样的列表：
spam = ['apples', 'bananas', 'tofu', 'cats']
编写一个函数，它以一个列表值作为参数，返回一个字符串。该字符串包含所有表项，表项之间以逗号和空格分隔，并在最后一个表项之前插入 and。
例如，将前面的 spam 列表传递给函数，将返回'apples, bananas, tofu, and cats'。
但你的函数应该能够处理传递给它的任何列表。
"""
spam = ['apples', [1,2],'bananas', ('a','b'),'tofu',1,1.0, 'cats']

def func(myList):
    s=""
    for i in range(len(myList)-1):
        s += str(myList[i])+','
    s += 'and '+ myList[-1]
    print(s)

func(spam)



"""
假定有一个列表的列表，内层列表的每个值都是包含一个字符的字符串，像这样：
grid = [['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]
你可以认为 grid[x][y]是一幅“图”在 x、y 坐标处的字符，该图由文本字符组成。
原点(0, 0)在左上角，向右 x 坐标增加，向下 y 坐标增加。
复制前面的网格值，编写代码用它打印出图像。
..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....
"""

grid = [
['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']
]

for i in range(len(grid)):
    for j in range(len(grid[i])):
        print('('+str(i),str(j)+')',sep=',',end='\t')
    print()

for j in range(len(grid[0])):
    for i in range(len(grid)):
        print(grid[i][j],end='')
    print()