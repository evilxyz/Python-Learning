#!/usr/bin/env python
#encoding=utf-8

import sys

###################### 普通实现版 ###############################

def print3(*args, **kargs):
    sep = kargs.get('sep', ' ')          #以这种形式从**kargs取出参数, 若调用时没有给sep赋值, 则sep = ' '
    end = kargs.get('end', '\n')         #同上, 如果没给end赋值, end='\n'
    file=kargs.get('file', sys.stdout)   #输出流
    output = ''
    first = True
    
    for arg in args:
        output += ('' if first else sep) + str(arg)     #很巧妙, 判断是否是第一次进入循环,如果是,则返回'', 否则返回sep
        first = False
    file.write(output + end)

###################### keyword-only 实现版 #######################

def print30(*args, sep=' ', end='\n', file=sys.stdout):
    output = ''
    first = True

    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False

    file.write(output + end)

#这个没有排错功能的

##################### 无异常版 #####################################

def print300(*args, **kargs):
    sep = kargs.pop('sep', ' ')
    end = kargs.pop('end', '\n')
    file = kargs.pop('file', sys.stdout)
    if kargs: raise TypeError('extra keywords: %s' % kargs)
    output = ''
    first = True

    for arg in args:
        output += ('' if first else sep)+arg
        first = False
    file.write(output + end)

