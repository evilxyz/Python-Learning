#!/usr/bin/env python
#encoding=utf-8

x = 'evil.'
y = 'xyz'
z = 'It\'s me !'

if x:
    r = y
else:
    r = z

#上面的代码很简单,但写了四行... 其实在py中有个三元表达式, 我来示范

r = y if x else z   #意思就是如果x为真, r = y, 否则 r = z
