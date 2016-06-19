#!/usr/bin/env python
#encoding=utf-8

import shelve

db = shelve.open('persondb')

for key in sorted(db):
    print (key, '\t=>', db[key])    # db 中存储的是一个字典


sue = db['Sue Jone']

sue.giveRaise(.10)

db['Sue Jone'] = sue
