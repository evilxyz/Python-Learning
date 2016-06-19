#!/usr/bin/env python
#encoding=utf-8

"""
Climb inheritance trees using namespace links,
displaying higher superclasses with indentation
"""

def classtree(cls, indent):
    print ('.' * indent + cls.__name__)       #print class name here, same as Instance.__class__.__name__
    for supercls in cls.__bases__:            #Recur to all superclasses
        print (supercls)
        classtree(supercls, indent + 3)       #May visit super > once

def instancetree(inst):
    print ('Tree of {0}'.format(inst))
    classtree(inst.__class__, 3)            #Climb to its class

def selftest():
    class A:        pass
    class B(A):     pass
    class C(A):     pass
    class D(B, C):  pass
    class E:        pass
    class F(D, E):  pass
    
    instancetree(B())
    instancetree(F())

if __name__ == '__main__':
    selftest()
    

