#!/usr/bin/env python
#encoding=utf-8

#测试from test import x, y, printx, printy
#    from ... import ... 语句只是把其它模块中的变量名复制过来, 如上
# 如果在交互模式下修改x, y的值只是对本地作用域中的值修改, 而非对test模块中的变量进行修改
# 如果用import test 的话
# test.x = 10086
# test.y = 233
# 然后再使用test模块中的printx, printy函数进行输出x, y的值, 会发现已经改变

x = 2
y = 1

print ('Test Output')

def printx(): print (x)
def printy(): print (y)

def cout(txt):
    print (txt)
