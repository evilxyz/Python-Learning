#!/usr/bin/env python
#encoding=utf-8

()                      #空元组
T = (0,)                #包含一个元素的元组
T = (0, 'Ni', 1.2, 3)   #多元素元组
T = 0, 'Ni', 1.2, 3     #不加括号也可以哦, 但不推荐

T = ('abc', ('def', 'ghi')) #嵌套元组

print (T[0])
print (T[1][1])             #元组的索引

T2 = ('i am xyz', 18, 'man')

print ('T + T2 =', T+T2)    #合并
print ('T * 3 =', T*3)      #重复
print ('T[1:3] =', T[1:3])  #分片

T = tuple('spam')           #一个可迭代对象的项的元组

for x in T: print (x)       #迭代

print ('len', len(T))       #元组长度

print ('spam in T', 'spam' in T)    #成员关系

T = tuple(x + 2 for x in range(10, 15))

print (T)

T = tuple(x * 2 for x in [2, 4, 6, 8])   #迭代创建元组
print (T)

T = T+(12, 13, 14, 15)

print ('T.index(12)', T.index(12))       #索引
print ('T.count(12)', T.count(12))       #统计

T = (1, [2, 3], 4)

T[1][0] = 'I can changed'           #元组里面如果有列表或字典,那么可以改变
                                    #不可变性只适用于元组本身顶层,而并非其内容
print (T)
