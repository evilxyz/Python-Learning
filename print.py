#!/usr/bin/env python
#encoding=utf-8

import sys

x = 'xyz'
y = 12138
z = ['evil']

print ('---------------print test--------------\n')

print (x, y, z) 

# print ([object, ...][, sep=' '][, end='\n'][, file=sys.stdout])

#sep代表多个对象中间的间隔符,默认为空格
#end代表文本末尾的字符串, 默认为换行 
#file代表默认输出位置, 任何可写的对象都可以 exp: open('/tmp/txt.txt', 'w')


print (x, y, z, sep='', end='\t ending...\n') #对象中没有间隔,

print (x, y, z, sep='\n', file=open('/tmp/test.txt', 'w')) #输出位置改变为test.txt
print (open('test.txt', 'r').read())


print ('\n------------sys.stdout test-------------------\n')

sys.stdout.write(str(x) + ' ' + str(y) + '\n')  # sys.stdout.write等价于print (x, y)

temp = sys.stdout                               #备份sys.stdout以便后面恢复输出流
sys.stdout = open('/tmp/test.txt', 'a')         #重定向默认输出位置(/tmp/test.txt)

print ('I Just Test !\n')

sys.stdout.close()                              #记得手动关闭文件

sys.stdout = temp                               #恢复默认输出流(终端)

print ('hey, i am back !')


print ('/tmp/test.txt:\n', open('/tmp/test.txt', 'r').read())
