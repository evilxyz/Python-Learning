#!/usr/bin/env python
#encoding=gbk

def f(L, S):
    L[0] = '我最帅'
    S = 'test'

l = [1, 2, 3, 4, 'go', 'go', 'go']
s = 'evilxyz'   #因为这个s是全局变量(在模块顶层声明),和f函数内的s不冲突

f(l, s)         #可变参数通过指针赋值, 不可变参数通过"值"传递.
                #因此,可变对象作为参数, 在函数内修改会影响外部变量.
                #不可变对象作为参数, 则不会影响

print (l, s)

############## 参数内容是否可变测试 ################

def changer(L):
    L[0] = 'i can not change'

L = [1, 2]
changer(L[:])   #可以通过传递可变对象的拷贝,达到在函数内不可修改对象的目的

print (L)

############## other way

def changer1(L):
    L = L[:]    #在内部去拷贝, 这种方法应该更常用!
    L[0] = 'i can not change'

changer1(L)
print (L)


############# other way

def changer2(L):
    L[0] = ['i can not change']

changer2(tuple(L))      #这种方法很极端,会报错,因为元组不可以改变

print (L)

