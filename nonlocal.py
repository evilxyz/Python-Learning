#!/usr/bin/env python
#encodint=utf-8

def tester(start):
    state = start
    def nested(label):
        nonlocal state      #仅可以改变嵌套循环外层的变量(非全局变量), 变量必须存在
        state += 1
        print (state, label)
    return nested

F = tester(232)
F('spam')
