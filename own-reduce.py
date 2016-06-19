#!/usr/bin/env python
#encoding=utf-8

def myreduce(func, args):
    result = args[0]
    for second in args[1:]:
        result = func(result, second)
    return result  

print (myreduce((lambda x, y: x+y), [1, 2, 3]))
