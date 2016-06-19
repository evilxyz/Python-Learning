#!/usr/bin/env python
#encoding=utf-8

def echo(message):
    print (message)

echo('Direct call')     #直接调用

x = echo
x('Indirect call!')     #间接调用



def indirect(func, arg):
    func(arg)

indirect(echo, 'Argument call!')    #参数通过赋值对象来传递,就像是把函数作为参数传递给其他函数.


schedule = [ (echo, 'Spam!'), (echo, 'Eggs!') ]
for (func, arg) in schedule:        #可以把函数填入到数据结构中
    func(arg)

###################### 

def make(label):
    def echo(message):
        print (label + '+' + message)
    return echo

F = make('Spam')    #
F('Ham!')
F('evilxyz')
