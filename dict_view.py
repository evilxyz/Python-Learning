#!/usr/bin/env python
#coding=utf-8

D = {'a': 1, 'b': 2, 'c': 3}

view_key = D.keys()
view_val = D.values()

for x in view_key:
    print (x)

for x in view_val:
    print (x)

D.pop('b')          #视图会随着字典的改变而改变
D['d'] = 4


for x in view_key:
    print (x)

for x in view_val:
    print (x)

print (view_key & view_key)
print (view_key | view_key)     #D.keys()可以有交集和并集,因为键是惟一的, 而D.values()是不行的,因为值不惟一


D = {'x': 1, 'x': 3.14, 'x': 'Your Sister', 'y': 2, 'z': 3}    #如果一个字典里有多个相同键值, 会保留最后一个.Len(D) = 3

print ('\n\n', D)
