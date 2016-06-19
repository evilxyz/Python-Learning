#!/usr/bin/env python
#encoding=utf-8

print (list(range(5)))

print (list(range(0, 6)))

print (list(range(0, 10, 2)))

print (list(range(5, -5, -1)))

#range迭代器测试

R = range(10, 15)
I = iter(R)

print (next(I))     #输出0
print (list(R))     #输入0-10, list(R) 对range用强...全输出

print (len(R))
print (R[0], R[1], R[-1])
