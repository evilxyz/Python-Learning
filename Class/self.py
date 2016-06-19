#!/usr/bin/env python
#encoding=utf-8

# self ���õ��ǵ�ǰ���ڴ����ʵ��

class NextClass:                #define class
    def printer(self, text):    #define method
        self.message = text     #change instance
        print (self.message)    #access instance

x = NextClass()
x.printer('evilxyz')            #equal  NextClass.printer(x, 'evilxyz')

print (x.message)               #x got a message

NextClass.printer(x, 'Direct Call')

print (x.message)


print ('-' * 30)

################ ��д�̳з��� #####################

class Super:
    def method(self):
        print ('in Super.method')

class Sub(Super):
    def method(self):                   #overwrite
        print ('sarting Sub.method')
        Super.method(self)              #direct call Super.method, self����ǰ����
        print ('ending Sub.method')

s = Sub()
s.method()

