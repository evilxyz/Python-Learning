#!/usr/bin/env python
# encoding=utf-8

class Super:
    def method(self):
        print('in Super.method')
    def delegate(self):     # 期待子类实现接口
        self.action()       # 调用子类的action函数
    def action(self):
        assert False, 'action must be defined!'     # 如果子类的action函数未定义, 则会调用超类的action函数引发错误

class Inheritor(Super):
    pass

class Replacer(Super):
    def method(self):
        print('in Replacer.method')

class Extender(Super):
    def method(self):
        print('in Extender.method')
        Super.method(self)
        print('out Extender.method')

class Provider(Super):
    def action(self):
        print('in Provide.action')

if __name__ == '__main__':
    for klass in (Inheritor, Replacer, Extender):
        print('\n' + klass.__name__ + '...')    # 类的 __name__ 属性为当前类的名字, 实例的Instance.__class__.__name__
        klass().method()                        # 可显示出类名字
    print('\nProvider...')
    x = Provider()
    x.delegate()
