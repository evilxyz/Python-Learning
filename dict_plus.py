#!/usr/bin/env python
#coding=utf-8

# 字典解析生成字典

D = {x: x ** 2 for x in [1, 2, 3, 4]}
print (D)


D = {x: x * 4 for x in 'spam'}
print (D)

D = {c.lower(): c + '!' for c in ['SHIT', 'FUCK', 'DAMN']}
print (D)


# fromkeys 生成字典
D = dict.fromkeys(['a', 'b', 'c'], 0)   #用键初始化字典
print (D)

D = {k:0 for k in ['a', 'b', 'c']}      #和上面效果一样, 使用字典解析来创建字典
print (D)

D = dict.fromkeys('spam')
print (D)

D = {k:None for k in 'spam'}
print (D)
