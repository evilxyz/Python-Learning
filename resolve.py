#!/usr/bin/env python
#encoding=utf-8

print ( [x * x for x in range(10)] )  #列表解析

print ( (x * x for x in range(10)) )  #生成器表达式

print ( {x * x for x in range(10)} )  #集合解析

#等同于 set( x * x for x in range(10) )


print ( {x: x*x for x in range(10)} ) #字典解析

#等同于 dict( (x, x * x) for x in range(10) )



print ( [x * x for x in range(10) if x % 2 == 0] )      #列表是排序的

print ( {x * x for x in range(10) if x % 2 == 0} )      #但是集合不是

print ( {x: x * x for x in range(10) if x % 2 == 0} )   #字典也一样

print ( {x + y for x in 'ab' for y in 'cd'} )           #集合解析嵌套

print ( {x + y: (ord(x), ord(y)) for x in 'ab' for y in 'cd'} )

print ( {x.upper(): x * 2 for x in ['evil', 'xyz']} )
