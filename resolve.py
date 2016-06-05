#!/usr/bin/env python
#encoding=utf-8

print ( [x * x for x in range(10)] )  #�б����

print ( (x * x for x in range(10)) )  #���������ʽ

print ( {x * x for x in range(10)} )  #���Ͻ���

#��ͬ�� set( x * x for x in range(10) )


print ( {x: x*x for x in range(10)} ) #�ֵ����

#��ͬ�� dict( (x, x * x) for x in range(10) )



print ( [x * x for x in range(10) if x % 2 == 0] )      #�б��������

print ( {x * x for x in range(10) if x % 2 == 0} )      #���Ǽ��ϲ���

print ( {x: x * x for x in range(10) if x % 2 == 0} )   #�ֵ�Ҳһ��

print ( {x + y for x in 'ab' for y in 'cd'} )           #���Ͻ���Ƕ��

print ( {x + y: (ord(x), ord(y)) for x in 'ab' for y in 'cd'} )

print ( {x.upper(): x * 2 for x in ['evil', 'xyz']} )
