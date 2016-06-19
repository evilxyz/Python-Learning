#!/usr/bin/env python
#encoding=utf-8



def intersect(x, y):
    return set(x) & set(y) 

print (intersect('evilxyz', 'ilxy'))        #Good Way
print (intersect([1, 2, 3], (1, 4)))



#answer other way

L = []

def intersect2(x, y):
    for c in x:
        if c in y:
            L.append(c)
    return L

print (intersect2('testintersect', 'tint'))

#another way

x = 'administrator'
y = 'admxxxxxxxxor'
print ([c for c in x if c in y])
