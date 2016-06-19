#!/usr/bin/env python
#encoding=utf-8

L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]

print (list(zip(L1, L2)))

for (a, b) in zip(L1, L2):
    print (a, b)


#如果长度不一致, 会舍弃多出的字符

S1 = 'evil'
S2 = 'xyz'

print (list(zip(S1, S2)))


###### 用zip构造字典

keys = ['one', 'two', 'three', 'four', 'five']
vals = [1, 2, 3, 4, 5]

D = dict(zip(keys, vals))

print (D)


###### 迭代测试
print ('\n\n迭代测试\n')

Z = zip((1, 2, 3), ('x', 'y', 'z'))

print (list(Z)) #第一次可以输出
print (list(Z)) #第二次就没有了,因为map, zip, filter迭代器特性, 遍历结果一次后,它们就用尽了
                #所以会返回空列表

Z = zip((1, 2, 3), ('x', 'y', 'z'))

for z in Z:
    print ('z ==>', z)  #重新赋值后, 又可以遍历出来

############### 疯狂的 zip ##################

print ("疯狂的 zip")

def myzip(*seqs):
    seqs = [list(S) for S in seqs]
    res = []
    while all(seqs):                                #all(), 只要列表或元组中有一个为假,则为假
                                                    #S.pop(0) for S in [['x', 'y', 'z'], [1, 2, 3]]
        res.append(tuple(S.pop(0) for S in seqs))  #因为S是列表,所以可以改变,每次取出第一个元素
    return res

print (myzip(['x', 'y', 'z'], [1, 2, 3]))
print (myzip(['x', 'y', 'z'], [None, None, None]))


def myzip1(*seqs, pad=None):                        #如果参数长度不一致,支持设置默认参数(默认参数默认为None
    seqs = [list(S) for S in seqs]                  #把seqs中的内容转成列表类型
    res = []
    while any(seqs):                                #只要seqs中有一个为真
        res.append(tuple((S.pop(0) if S else pad) for S in seqs))   #三元运算, 如果S为真,返回S.pop(0),否则返回pad
    return res      #一般zip转换为元组,因为易于函数调用

print (myzip1('evilxyz', 'admin'))
print (myzip1('test', 'xyz', pad='$'))

def myzip2(*seqs, pad=None):
    seqs = [list(S) for S in seqs]
    res = []
    while any(seqs):              
        yield tuple((S.pop(0) if S else pad for S in seqs))     #生成器函数返回的是一个支持迭代协议的生成器对象

print (list(myzip2('passwd', 'xyz')))
print (list(myzip2('passwd', 'aaa')))   

def myzip3(*seqs):                                              #根据最小长度来截取
    minlen = min(len(S) for S in seqs)  #求出最小长度
    return [tuple(S[i] for S in seqs) for i in range(minlen)]

print (myzip3('balabala', 'xyz'))


def myzip4(*seqs, pad=None):
    maxlen = max(len(S) for S in seqs)
    return [tuple(S[i] if len(S) > i else pad for S in seqs) for i in range(maxlen)]
"""
for i in range(maxlen):
    for S in seqs:
        if len(S) > i:
            S[i]
        else:
            pad

"""
print (myzip4('evilxyz', 'pass'))
print (myzip4('evil', 'aa', pad='*'))

def myzip5(*args):
    iters = list(map(iter, args))
    while iters:
        res = [next(i) for i in iters]      #tuple(['e', 'x'])
        yield tuple(res)

print (list(myzip5('evil', 'xyz')))
