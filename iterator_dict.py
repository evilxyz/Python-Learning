#!/usr/bin/env python
#encoding=utf-8

D = dict(x=1, y=2, z=3)

I = iter(D)         #�൱�� iter(D.keys())

print (next(I))
print (next(I))     #�ֶ�����

for k in sorted(D): print (k, D[k])     #sorted(D)�൱��sorted(D.keys())

for (k, v) in D.items(): print (k, v, end=' ')
