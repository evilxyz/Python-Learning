#!/usr/bin/env python
#encoding=utf-8

import sys
import timer

reps = 1000
repslist = range(reps)

def forLoop():
    res = []
    for x in repslist:
        res.append( x+10 )
    return res

def listComp():
    return [x+10 for x in repslist]

def mapCall():
    return list(map(lambda x: x+10, repslist))

def genExpr():
    return list(x+10 for x in repslist)

def genFunc():
    def gen():
        for x in repslist:
            yield x+10

    return list(gen())          #gen()����һ�����οɵ�������,��listǿ����ʾ

#��������ú����������ý�����map
#������Զ��庯���������ý������б����


print (sys.version)
for tester in (timer.total, timer.bestoftotal):
    print ('<{0}>'.format(tester.__name__))
    for test in (forLoop, listComp, mapCall, genExpr, genFunc):
          elapsed, result = tester(test, _reps=reps)
          print ('-' * 33)
          print ('{0:<9}: {1:.6f} ===> [{2}...{3}]'.format(test.__name__, elapsed, result[0], result[-1]))
