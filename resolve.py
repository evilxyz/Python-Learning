#!/usr/bin/env python
#encoding=utf-8

print ( [x * x for x in range(10)] )     # 列表解析

print ( (x * x for x in range(10)) )     # 生成器表达式

print ( {x * x for x in range(10)} )     # 集合解析
# 等同
print ( set( x * x for x in range(10) ) )# 集合解析


print ( {x: x*x for x in range(10)} )           # 字典解析
#等同
print ( dict( (x, x * x) for x in range(10) ) ) # 字典解析



print ( [x * x for x in range(10) if x % 2 == 0] )      # 列表解析带条件, 有序输出

print ( {x * x for x in range(10) if x % 2 == 0} )      # 集合解析带条件, 无序输出

print ( {x: x * x for x in range(10) if x % 2 == 0} )   # 字典解析带条件, 无序输出

print ( {x + y for x in 'ab' for y in 'cd'} )           # 集合解析嵌套

print ( {x + y: (ord(x), ord(y)) for x in 'ab' for y in 'cd'} )

print ( {x.upper(): x * 2 for x in ['evil', 'xyz']} )
