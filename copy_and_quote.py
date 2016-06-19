#!/usr/bin/env python
#encoding=gb2312


X = [1, 2, 3]
L = ['a', X, 'b']   #引用X
D = {'x':X, 'y':2}  #字典引用X

print('-' * 30, '引用可变对象', '-' * 30)

print ('当前X, L, D 值为:\n')
print ('X=', X, '\n', 'L=', L, '\n', 'D=', D, sep='')

X[1] = 'God' 

'''
    X = ['2', '3', '4', '5']
    问题? 为什么这样赋值L和D不会改变呢
    因为是直接改变的X的对象
'''
print('\n')

print ('改变X[1]后, X, L, D 值为\n')
print ('X=', X, '\n', 'L=', L, '\n', 'D=', D, sep='')


print ('\n\n')
print('-' * 30, '拷贝可变对象', '-' * 30)

X = [1, 2, 3]
L = ['a', X[:], 'c']
D = {'x': X.copy(), 'y': 2}     #拷贝, 而不是引用,如果是引用,在原处修改会改变引用它的对象

print ('当前X, L, D 值为:\n')
print ('X=', X, '\n', 'L=', L, '\n', 'D=', D, sep='')

X[1] = 'kindness'

print('\n')

print ('改变X[1]后, X, L, D 值为\n')
print ('X=', X, '\n', 'L=', L, '\n', 'D=', D, sep='')
