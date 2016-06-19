#!/usr/bin/env python
#encoding=utf-8

for line in open('iterator.py', 'r'):
    print (line.upper())                            #I can read myself



D = {'x':'evil.xyz', 'y':3.1415926, 'z':'it\'s me'}
I = iter(D)                       #从字典获取迭代器

for keys in D:
    print (keys, D[keys])

###### range 迭代测试 #######

R = range(5)
I = iter(R)

print (next(I))
print (next(I))


##### Other Iterator ######

print (list( map(str, open('test.txt')) ))        
print ( 'Just don\'t give up\n' in open('test.txt'))    #成员运算
#成员运算也会使用迭代协议, 逐行扫描
print (sorted(open('test.txt')) )

print (list(zip(open('test.txt'), open('test.txt'))))
print (list(enumerate(open('test.txt'))))               # 0对应第一行, 1对就第二行, 以此类推

print (sum([3, 2, 4, 5, 6, 7, 9]))
print (any(['evil.xyz', 3.14, '', None]))       #任意一个元素为真,即为真
print (all(open('test.txt')))                   #测试test.txt有没有空值
print (max([3, 4, 5, 2, 1]))
print (min([3, 4, 5, 2, 1]))
print (max(open('test.txt')))
print (min(open('test.txt')))


print ('&&'.join(open('test.txt')))


x, y, *z = open('test.txt')
print ('########\n', x, y, z)



# map, zip, filter 拥有自己的迭代器, 在遍历其结果一次后, 它们就用尽了,即不能多次重复使用结果

print ('-' * 30, 'map 基本操作', '-' * 30)

M = map(abs, range(-5, 5))    #map return an iterator, not a list

print (list(M))             #output once
print (list(M))             #output twice, but empty list


M = map(abs, range(-5, 5))
print (next(M))             #手动控制输出, 其实是调用M.__next__()


