#!/usr/bin/env python
#encoding=utf-8

print ( (x ** 2 for x in range(5)) )        #生成器表达式, 不同于[x ** 2 for x in range(5)]

print ( list((x ** 2 for x in range(5))) )  #list强制显示

G = (x ** 2 for x in range(5))              #产生一个生成器对象

print (next(G))
print (next(G))

for num in (x ** 2 for x in range(4)):      #生成器自身的括号不是必须的,前提是在其它函数调用之中
    print ('%s, %s' % (num, num / 2.0))


print ( x ** 2 for x in range(5) )          #可以省略括号

print ( sum( x ** 2 for x in range(4) ) )

print (sorted((x ** 2 for x in range(4)), reverse=True))    #需要括号

from math import sqrt

print (list(map(sqrt, (x ** 2 for x in range(4)))))               #需要括号
