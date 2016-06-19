#!/usr/bin/env python
#encoding=utf-8

import sys
import time

reps = 1000         #reps��ȫ�ֱ���
repslist = range(reps)

def timer(func, *pargs, **kargs):
    start = time.clock()            #Get System Clock
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = time.clock() - start

    return (elapsed, ret)

###########  The Best ########################################


timer = time.clock if sys.platform[:3] == 'win' else time.time     #��linuxƽ̨��,time.time����


def total(func, *pargs, _reps=1000, **kargs):    #Keywords , Py3.x Only
    
    start = timer()
    for i in range(_reps):
        ret = func(*pargs, **kargs)
    elapsed = timer() - start
    return (elapsed, ret)

def bestof(func, *pargs, _reps=5, **kargs):
    
    best = 2 ** 32          #136 years seems large enough

    for i in range(_reps):   #range usage not timed here
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
        if elapsed < best: best=elapsed
    return (best, ret)

def bestoftotal(func, *pargs, _reps1=5, **kargs):
    return min(total(func, *pargs, **kargs) for x in range(_reps1))         #ѭ��5��,����С, for x in range(_reps1)
                                                                            #��������ѭ������....
