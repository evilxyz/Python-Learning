#!/usr/bin/env python
#coding=utf-8

import sys

s = 'Hex:{0:>10X}\nOct:{1:>10o}\nBin:{2:>10b}\n'.format(255, 255, 255)

# {0:>10X} 表示第0个参数 10个字符宽度并且右对齐

print (s)




print ('My {1[spam]:<8} runs {0.platform:>8}'.format(sys, {'spam':'laptop'}))



data = dict(spam='laptop', platform=sys.platform)

print ('My {spam:<8} runs {platform:>8}'.format(**data))    #参数0八个字符位宽,左对齐.  参数0 laptop, 参数1 sys.platform




print ('{0:d}'.format(9999999999))
print ('{0:,d}'.format(9999999999))
print ('{0:,.2f}'.format(1234.567))                 #三位数会用逗号分隔,并保留两位小数


print ('{} {} {} ?'.format('who', 'am', 'i'))       #也可以不加数字偏移量
