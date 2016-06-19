#!/usr/bin/env python
#encoding=utf-8

Z = zip((1, 2, 3), ('x', 'y', 'z'))

I = iter(Z)
II= iter(Z)

print (next(I))
print (next(II))    #输出I会影响II, 这是因为zip, map, filter一样, 都会在遍历一次结果后, 它们就用尽了
print (next(I))


#生成器是单迭代对象, 即遍历一次后就会用尽

#生成器表达式测试

G = (c * 4 for c in 'evil')

print (iter(G) is G)

I1 = iter(G)
I2 = iter(G)

print (next(I1))
print (next(I1))
print (next(I2))
print (next(I2))

#生成器函数测试

def timesfour(S):
    for c in S:
        yield c * 4

G = timesfour('xyz')

I1, I2 = iter(G), iter(G)

print (next(I1))
print (next(I2))
