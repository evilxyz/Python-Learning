#!/usr/bin/env python
#encoding=utf-8

import sys


print('-' * 30, 'lambda 简单应用', '-' * 30)

f = lambda x, y, z: x + y + z   # 等同于 def f(x, y, z): return x+y+z

print( f(1, 2, 7) )


x = (lambda a="fee", b="fie", c="foe": a+b+c)   # lambda使用默认值

print( x() )

 
print('-' * 30, 'lambda 嵌入到函数', '-' * 30)

def func(x):
    return (lambda n=10: x ** n)     # 基数为x

x = func(10)    # x = 10

print ( x(2) )  # n = 2
print ( x() )   # n = 10(默认值)


print('-' * 30, 'lambda 嵌入到列表', '-' * 30)

L = [lambda x: x**2, 
     lambda x: x**3,
     lambda x: x**4]

for f in L:
    print( f(2) )

print (L[0](10))    #也可以直接调用


print('-' * 30, 'lambda 高级应用', '-' * 30)

lower = (lambda x, y: x if x < y else y)

print (lower('aa', 'bb'))


show_all_v1 = lambda x: list(map(sys.stdout.write, x))
# 等同
show_all_v2 = lambda x: [sys.stdout.write(line) for line in x]

show_all_v1(('evil\n', 'xyz\n'))    #把元组赋给x, 其实列表也可以的
show_all_v2(('evil\n', 'xyz\n')) 

func = lambda: print ('test')       #定义无参 lambda func

func()
