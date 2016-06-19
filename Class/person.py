#!/usr/bin/env python
#encoding=utf-8

from classtools import AttrDisplay

class Person(AttrDisplay):
    """
    Create and process person records
    """

    def __init__(self, name, job='None', pay=0):    #构造函数, 表问我为什么job不是None而是'None' format不支持打印None
        self.name = name
        self.job = job
        self.pay = pay
    

#    def __str__(self):            #打印Person实例的时候,会自动调用__str__, 但不具备灵活性, 代由classtools中类实现
#        return '{0:<10} {1:<15} {2:<15} {3:<10}'.format(self.__class__.__name__, self.name, self.job, self.pay)


                                                        #实例去引用类的属性,打印父类名

    def lastName(self):
        return self.name.split()[-1]                #返回名字

    def giveRaise(self, percent):                   #涨工资
        self.pay = int(self.pay * (1 + percent))


class Manager(Person):
    """
    A customized Person with special requirements
    """

    def __init__(self, name, pay):                  #refine __init__ , job not nedded
        Person.__init__(self, name, 'mgr', pay)
        
    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)     #向上继承


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='developer', pay=100000)

    print ('{0:<15} {1:<15} {2:<10}'.format(bob.name, bob.job, bob.pay))
    print ('{0:<15} {1:<15} {2:<10}'.format(sue.name, sue.job, sue.pay))    #常规输出

    print ('-' * 40)
    print ('bob.lastName() ===> ' + bob.lastName(), 'sue.lastName() ===> ' + sue.lastName(), sep='\n')

    sue.giveRaise(.10)
    print ('Now, Sue.pay ===> ', sue.pay)

    print ('-' * 40)
    print (sue)
    
    print ('-' * 40)
    tom = Manager('Tom Jones', 50000)               #define tom is a manager
    tom.giveRaise(.10)                              #Raise

    print ('{0:<15} {1:<15} {2:<10}'.format(tom.name, tom.job, tom.pay))

    
    print ('--All three--')

    for obj in (bob, sue, tom):
        obj.giveRaise(.20)
        print (obj)

    print ('--All End --')

    for key in tom.__dict__:                        # 每个实例默认都有__dict__属性, 带有键/值(很有用)
        print (key, '===>', tom.__dict__[key])
