#!/usr/bin/env python
#encoding=utf-8

R = range(3)
I = iter(R)

print (next(I)) #输出一个元素
print (next(I))
print (next(I))

II = iter(R)    #测试是否支持多个迭代器

print (next(II))
print (next(II))

#列表测试
print ('List Test')

L = [1, 2, 3, 4]
I1, I2 = iter(L), iter(L)

print (next(I1))
print (next(I2))

del L[2:]

print (next(I1))
print (next(I1))        #会提示 StopInteration, 列表支持多个抚今迭代器, 并且在一个活动迭代器中反映它们的原处修改
