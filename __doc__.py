#!/usr/bin/env python
#encoding=utf-8

# 通过 module.class.method.__doc__ 来取出模块中类的方法函数的文档字符串

import sys

print (sys.__doc__)
print (sys.getrefcount.__doc__)

print (int.__doc__)     # 通过文档字符串读取内置函数的说明
print (map.__doc__)
