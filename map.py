#!/usr/bin/env python
#encoding=utf-8

print ('-' * 30, 'map 基本操作', '-' * 30)

print('1, 使用内置函数进行处理', end='\n\n')

print (list( map(abs, range(-5, 5) )))  # map return an iterator, not a list 

#并行返回每个序列中的元素作为函数对应参数得到的结果的列表
print (list( map(pow, [1, 2, 3, 4, 5], [2, 3, 4, 5, 6]) ))

print('2, 使用自定义函数进行处理', end='\n\n')

def inc(x): 
    return x+10

print (list( map(inc, range(-5, 5) )))

print('3, 使用lambda 进行处理', end='\n\n')
print (list( map(lambda x: x+10, range(-5, 5) )))
