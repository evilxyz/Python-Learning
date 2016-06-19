#!/usr/bin/env python
#encoding=utf-8

from person import Person, Manager
import shelve                           #shelve 存储永久模块

bob = Person('Bob Smith')
sue = Person('Sue Jone', job='developer', pay=100000)
tom = Manager('Tom Jone', 5000)

db = shelve.open('persondb')

for obj in (bob, sue, tom):
    db[obj.name] = obj          #以字典的形式, obj.name作为键, 整个obj作为值

db.close()

db = shelve.open('persondb')

for obj in db:
    print (db[obj])             #输出
    print(obj)
    

db.close()
