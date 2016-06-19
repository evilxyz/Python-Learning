#!/usr/bin/env python
#encoding=utf-8

def min1(*args):
    res = args[0]
    for arg in args[1:]:
        if arg < res:
            res = arg


    return res

def min2(*args):
    return sorted(list(args))[0]    #一行搞定... 求最大值返回 [-1]

print (min1(5, 4, 1, 2, 9))
print (min2(5, 3, 7, 9, 6))


