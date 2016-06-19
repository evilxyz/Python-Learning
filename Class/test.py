#! /usr/bin/env python
# encoding=utf-8

from classtools import AttrDisplay

class Person(AttrDisplay):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    # def __str__(self):
        # return '{0} is my name, my job is {1} and my income is {2}'.format(self.name, self.job, self.pay)

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay *= (1 + percent)

class Manager(Person):
    def __init__(self, name, job='mgr', pay=0):
        Person.__init__(self, name, job, pay)

    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)     # good way

if __name__ == '__main__':

    bob = Person('Bob Smith', 'Worker', pay=999)
    tom = Person('Tom Anna', 'Worker')
    anna= Manager('Anna pig', pay=10000)

    bob.giveRaise(0.2)
    anna.giveRaise(0.2, bonus=0.3)
    
    for object in (bob, tom, anna):
        object.giveRaise(.10)
        print(object)

    # 各种类属性介绍
    print('-' * 40)

    print(anna.__class__)            # show anna's class and its name, instance --> class name
    print(anna.__class__.__name__)   # show anna's class

    print(anna.__dict__.keys())      # show anna's attributes
    print(anna.__dict__['name'])     # show anna's name

    print(Manager.__bases__)         # show super class

