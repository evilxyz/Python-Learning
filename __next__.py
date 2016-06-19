#!/usr/bin/env python
#encoding=utf-8

F = open('__next__.py', 'r')

#所有的迭代工具在内部工作起来都是在每次迭代的时候调用 __next__

print (F.__next__())
print (F.__next__())
print (F.__next__())

print (next(F))     #其实next(F) 等同于 F.__next__()

D = {'x':'evil.xyz', 'y':3.1415926, 'z':'it\'s me'}

I = iter(D)             #每个可迭代对象内都有一个迭代器,可以手动获取迭代器

for keys in D:
    print (keys, D[keys])
