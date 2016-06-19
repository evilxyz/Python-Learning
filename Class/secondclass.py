#!/usr/bin/env python
#encoding=utf-8

from firstclass import FirstClass

class SecondClass(FirstClass):
    def display(self):              #data没赋值的情况下,不可直接调用
        print ('===>', self.data)


if __name__ == '__main__':
    t = SecondClass()
    t.setdata('test')
    t.display()

#可以在交互模式下进行测试
# s = SecondClass()
# s.setdata('evil')
# s.display()
