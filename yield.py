#!/usr/bin/env python
#encoding=utf-8

def gensquars(N):   #生成器对象,支持迭代器协议
    for i in range(N):
        yield i**2  #每执行一次,控制权都要交给函数

for i in gensquars(5):
    print ('==>', i)

x = gensquars(4)    #x现在是一个可迭代的对象
print ('x ==>', x)  #得到的一个生成器对象,支持迭代器协议(有__next__ 方法)

print (next(x))     #和x.__next__() 是一样的效果
print (next(x))

########### 扩展生成器 send , next
print ('---------- send, next -----------')

def gen():
    for i in range(10):
        x = yield i
        print (x)

G = gen()

print (G.__next__())        #等同于next(G), 调用G.send(value)之前,必须next(G)来开始一个生成器
print (G.send(20))          #G.send(20) 把20发送给生成器G , 所以x = 20
                            #调用G.send(20)后,会恢复生成器的代码.
#print (G.send(99))
print (G.__next__())        #会返回一个None, 为什么 ?
