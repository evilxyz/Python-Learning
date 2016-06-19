#!/usr/bin/env python
#encoding=utf-8

def func(*args): print (args)   #支持任意多参数

func()
func(1)
func(1, 2, 3)

def func(**args): print(args)

func(x='evil', y='.', z='xyz')
func(**{'x': 1, 'y': 2, 'z': 3})

def func(x, *pargs, **kargs): print (x, pargs, kargs)

func(1, 2, 3, y='evil', z='...')    #关键字参数不能给 位置已经分配好值 的参数赋值, 否则会起冲突

############# depress parameter ####################

def func(x, y, z): print (x, y, z)

args = (1, 2)
args += (3, )

func(*args)

args = {'x': 'evil', 'y': 'xyz', 'z': ' !'}

func(**args)    #字典解包用**

############# advance ############################

def func(e, v, i, l): print (e, v, i, l)

func(*(1, 2), **{'i': ord('e'), 'l': ord('l')})     #字典解包后会把values赋给函数中对应的键(keys),
                                                    #所以字典中的keys必须和func中的参数一样

func(1, *(2, 3), **{'l': 4})                        #e = 1, v = 2, i = 3, l = 4

func(1, i = 3, *(2, ), **{'l': 4})

func(1, *(2, 3), l=4)

func(1, *(2, ), i=3, **{'l': 4})                   #位置匹配->关键字匹配->*匹配->**匹配
                                                   #这个对位置要求很严格...很严格...严格...


############ more advance #######################

def func(*args):
    print (args)

func(*open('/etc/issue'))   #   '*' 解包理论上支持可迭代对象


