#!/usr/bin/env python
#encoding=gb2312


X = [1, 2, 3]
L = ['a', X, 'b']   #����X
D = {'x':X, 'y':2}  #�ֵ�����X

print('-' * 30, '���ÿɱ����', '-' * 30)

print ('��ǰX, L, D ֵΪ:\n')
print ('X=', X, '\n', 'L=', L, '\n', 'D=', D, sep='')

X[1] = 'God' 

'''
    X = ['2', '3', '4', '5']
    ����? Ϊʲô������ֵL��D����ı���
    ��Ϊ��ֱ�Ӹı��X�Ķ���
'''
print('\n')

print ('�ı�X[1]��, X, L, D ֵΪ\n')
print ('X=', X, '\n', 'L=', L, '\n', 'D=', D, sep='')


print ('\n\n')
print('-' * 30, '�����ɱ����', '-' * 30)

X = [1, 2, 3]
L = ['a', X[:], 'c']
D = {'x': X.copy(), 'y': 2}     #����, ����������,���������,��ԭ���޸Ļ�ı��������Ķ���

print ('��ǰX, L, D ֵΪ:\n')
print ('X=', X, '\n', 'L=', L, '\n', 'D=', D, sep='')

X[1] = 'kindness'

print('\n')

print ('�ı�X[1]��, X, L, D ֵΪ\n')
print ('X=', X, '\n', 'L=', L, '\n', 'D=', D, sep='')
