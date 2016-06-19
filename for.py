#!/usr/bin/env python
#encoding=utf-8


print ('------------元组测试--------------\n')

T = [(1, 2), (3, 4), (5, 6)]

for (a, b) in T:
    print (a, b)

for x in T:
    print (x[0], x[1])  #手动解包, a, b = x 这样也是一样的.


for ((a, b), c) in [((1, 2), 3), ['XY', 99], ((7, 8), 9)]: #这样也可以
    print (a, b, c)

for (a, *b, c) in [(1, 2, 3, 4), ('balabala'), ('abcd')]:
    print (a, b, c)

print ('------------字典测试--------------\n')

D = {'x':'xyz', 'y':'evil.', 'z':4858}

for key in D:
    print (key, '=>', D[key])

for (key, value) in D.items():
    print (key, '->', value)



