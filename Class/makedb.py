#!/usr/bin/env python
#encoding=utf-8

from person import Person, Manager
import shelve                           #shelve �洢����ģ��

bob = Person('Bob Smith')
sue = Person('Sue Jone', job='developer', pay=100000)
tom = Manager('Tom Jone', 5000)

db = shelve.open('persondb')

for obj in (bob, sue, tom):
    db[obj.name] = obj          #���ֵ����ʽ, obj.name��Ϊ��, ����obj��Ϊֵ

db.close()

db = shelve.open('persondb')

for obj in db:
    print (db[obj])             #���
    print(obj)
    

db.close()
