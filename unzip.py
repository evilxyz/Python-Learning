#!/usr/bin/env python
#encoding=utf-8

x = 1, 2
y = 3, 4

print (list(zip(x, y)))

a, b = (zip(*zip(x, y)))

print (a, b)
