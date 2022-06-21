# -*- coding:utf-8 -*-
# @author Kuangjm
# @date 2022/1/7
# @file 01_字典的增删改查.py

"""
字典是不排序的，所以不能像列表那样切片。
"""

l1 = [1,2,3]
l2 = [3,2,1]
print(l1 == l2)

d1 = {"f1":1,"f2":2,"f3":3}
d2 = {"f3":3,"f2":2,"f1":1}
print(d1 == d2)

d = {"f1":1,"f2":2,"f3":3}

for i in d.keys():
    print(i)

for i in d.values():
    print(i)

for i in d.items():
    #tuple类型
    print(i)


"""
增
"""
d = {"f1":1}
print(d)
d['f2'] = 2
print(d)


"""
多重赋值技巧
"""
for k,v in d.items():
    #tuple类型
    print('Key: ' + k + ' Value: ' + str(v))

print(d.keys())
print(list(d.keys()))

"""
删
"""

del d['f1']  # 删除键是'Name'的条目
print(d)
d.clear()      # 清空字典所有条目
print(d)
del d         # 删除字典
#print(d)


"""
检查字典中是否存在键或值
"""
d = {"f1":1,"f2":2,"f3":3}

print("f1" in d)
#等价于
print("f1" in d.keys())

print(1 in d.values())

print(("f1",1) in d.items())


"""
查
get()方法，它有两个参数：要取得其值的键，以及如果该键不存在时，返回的备用值。
"""
d = {"f1":1,"f2":2,"f3":3}
print(d["f2"])
print(d.get("f2"))

#print(d["f4"]) #KeyError: 'f4'
print(d.get("f4")) #None

print(d.get("f4",4))


"""
setdefault()方法提供了一种方式，在一行中完成这件事。
传递给该方法的第一个参数，是要检查的键。
第二个参数，是如果该键不存在时要设置的值。如果该键确实存在，方法就会返回键的值。
"""
d = {"f1":1,"f2":2,"f3":3}

if "f4" not in d:
    d['f4'] = 4
print(d)

#等价于
d = {"f1":1,"f2":2,"f3":3}
d.setdefault("f1",4)
d.setdefault("f4",4)
print(d)

"""
计算一个字符串中每个字符出现的次数。
"""
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

count = {}
for i in message:
    count.setdefault(i,0)
    count[i] = count[i] + 1
print(count)

"""
漂亮的打印
"""
import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

count = {}
for i in message:
    count.setdefault(i,0)
    count[i] = count[i] + 1
pprint.pprint(count)

d = {"f1":[1,2,3,4],"f2":d1,"f3":d2}

print(d)
pprint.pprint(d)

s = pprint.pformat(d)
print(s)
print(type(s)) #<class 'str'>

