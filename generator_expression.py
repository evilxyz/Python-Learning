#!/usr/bin/env python
#encoding=utf-8

print ( (x ** 2 for x in range(5)) )        #���������ʽ, ��ͬ��[x ** 2 for x in range(5)]

print ( list((x ** 2 for x in range(5))) )  #listǿ����ʾ

G = (x ** 2 for x in range(5))              #����һ������������

print (next(G))
print (next(G))

for num in (x ** 2 for x in range(4)):      #��������������Ų��Ǳ����,ǰ������������������֮��
    print ('%s, %s' % (num, num / 2.0))


print ( x ** 2 for x in range(5) )          #����ʡ������

print ( sum( x ** 2 for x in range(4) ) )

print (sorted((x ** 2 for x in range(4)), reverse=True))    #��Ҫ����

from math import sqrt

print (list(map(sqrt, (x ** 2 for x in range(4)))))               #��Ҫ����
