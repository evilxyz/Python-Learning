#!/usr/bin/env python
#encoding=utf-8



print('-' * 30, '疯狂编写自己的map函数', '-' * 30)


def mymap(func, seq):   #如果对pow这类多参的函数会无能为力
    res = []
    for x in seq:
        res.append(func(x))
    return res

print (mymap(lambda x: x+10, counters))

def mymap1(func, *seqs):
    res = []
    for args in zip(*seqs):         #类似这样的调用 mymap( pow, [1, 2, 3], [4, 5, 6] )
        res.append(func(*args))     #关于这为什么使用func(*args) 因为args需要解包,
                                    #不解包的状态为(-2,)(-1,)(0,)(1,)(2,), 解包后则会去掉括号和逗号,下面是测试代码
                                    #for x in zip([1, 2, 3]): print (x)
                                    #for x in zip([1, 2, 3]): print (*x)
    return res
print (mymap1( abs, [-2, -1, 0, 1, 2] ))            
print (mymap1( pow, [1, 2, 3], [4, 5, 6] ))


def mymap2(func, *seqs):
    return [func(*args) for args in zip(*seqs)]

print (mymap2( abs, [-2, -1, 0, 1, 2] ))            
print (mymap2( pow, [1, 2, 3], [4, 5, 6] ))

def mymap3(func, *seqs):
    res = []
    for args in zip(*seqs):
        yield func(*args)           #生成器函数返回一个迭代器

print (list(mymap3( abs, [-2, -1, 0, 1, 2] )))            
print (list(mymap3( pow, [1, 2, 3], [4, 5, 6] )))   #list强制显示

def mymap4(func, *seqs):
    return (func(*args) for args in zip(*seqs))     #生成器表达式

print (list(mymap4( abs, [-2, -1, 0, 1, 2] )))            
print (list(mymap4( pow, [1, 2, 3], [4, 5, 6] )))   #list强制显示

