#!/usr/bin/env python
#coding=utf-8

D = {}      #空字典

D = {'spam': 2, 'eggs': 3}  #两项目字典

D = {'food': {'ham': 1, 'egg': 2}}  #嵌套字典
D['food']['ham']                 

D = dict.fromkeys(['a', 'b'])   #方法构造

D = dict(zip('test', 'abc'))   #关键字, D = {'t': 'z', 'e': 'b', 's': 'c'}


D = dict(name='Bob', age=42)

D['name']                        #对键进行索引

print ('eggs' in D)             #成员关系:键存在测试

D.keys()                #方法:返回所有的键
D.values()              #方法:返回所有的值
D.items()               #方法:返回所有的键和值

D.copy()                #创建副本

print (D)
D.get('age1', 'really not in')     #如果键不存在,返回default

D2 = {'test': 'i am a dict'}
D.update(D2)            #字典合并, 会强制覆盖D内相同键的值!

D.pop('age')              #删除指定元素

print (len(D))          #元素个数

D['age'] = 42             #增加/修改; 如果key不是字典里面的元素则创建新的元素,否则修改key值

del D['age']              #删除元素

list(D.keys())          #字典视图

D.keys() & D2.keys()    #找出相同的集合
D.keys() | D2.keys()    #并集操作,返回结果类型为set()

D = {x: x*2 for x in range(10)} #字典解析


D = dict(zip(['a', 'b', 'c'], [1, 2, 3]))   #创建一个{'a':1, 'b':2, 'c':3}字典


