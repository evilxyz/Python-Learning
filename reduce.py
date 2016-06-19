#!/usr/bin/env python
#encoding=utf-8

from functools import reduce

show = reduce((lambda x, y: x+y), ['evil', 'xyz', 'is', 'me'])  

'''
reduce的arg1去对arg2中的可迭代元素去遍历(执行对应arg1中的操作)
'''

print (show)
