#!/usr/bin/env python
#encoding=utf-8

class C2:
    pass

class C3:
    pass

class C0(C2, C3):
    def __init__(self, who):    #构造函数, 可以直接引用name属性
        self.name = who

class C1(C2, C3):               #C2, C3是超类, C1继承C2, C3
    def setname(self, who):     #相当于java里面this, 声明setname方法
        self.name = who


I0 = C0('xyz')
I1 = C1()
I2 = C1()

I1.setname('Bob')
I2.setname('John')

print (I1.name, I2.name)
print (I0.name)

print ('-' * 30)


class Test():
    pass

Test.var = 233      #如果这个变量在类内找不到,会自动创建
print (Test.var)
