#!/usr/bin/env python
#encoding=utf-8

def multiple(x, y):
    x = 2
    y = [3, 4]
    return x, y     # return a tuple(put multiple values in tuple)

x = 1
l = [2, 3]

x, l = multiple(x, l)   # equal   x, l = (2, [3, 4])


print (x, l)
