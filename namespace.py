#!/usr/bin/env python
#encoding=utf-8

X = 11              #Global (module) name|attribute (X, or manaynames.X)

def f():            
    print (X)       #Access global X

def g():
    X = 22          #Local (function) variable (X, hides module X)
    print (X)

class C:
    X = 33          #Class attribute (C.X)
    def m(self):
        X = 44      #Local variable in method (X)
        self.X = 55 #Instance attribute (instance.X)

if __name__ == '__main__':

    print (X)   # 11
    f()         # 11
    g()         # 22
    obj = C()
    print (obj.X)   # 33
    obj.m()
    print (obj.X)   # 55    因为运行了m方法,所以 self.X = 55, self就是obj
    print (C.X)     # 33    实例和类不在一个命名空间,所以实例改变,类不改变
