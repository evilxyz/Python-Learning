#!/usr/bin/env python
#encoding=utf-8

import sys

x = 'xyz'
y = 12138
z = ['evil']

print ('---------------print test--------------\n')

print (x, y, z) 

# print ([object, ...][, sep=' '][, end='\n'][, file=sys.stdout])

#sep�����������м�ļ����,Ĭ��Ϊ�ո�
#end�����ı�ĩβ���ַ���, Ĭ��Ϊ���� 
#file����Ĭ�����λ��, �κο�д�Ķ��󶼿��� exp: open('/tmp/txt.txt', 'w')


print (x, y, z, sep='', end='\t ending...\n') #������û�м��,

print (x, y, z, sep='\n', file=open('/tmp/test.txt', 'w')) #���λ�øı�Ϊtest.txt
print (open('test.txt', 'r').read())


print ('\n------------sys.stdout test-------------------\n')

sys.stdout.write(str(x) + ' ' + str(y) + '\n')  # sys.stdout.write�ȼ���print (x, y)

temp = sys.stdout                               #����sys.stdout�Ա����ָ������
sys.stdout = open('/tmp/test.txt', 'a')         #�ض���Ĭ�����λ��(/tmp/test.txt)

print ('I Just Test !\n')

sys.stdout.close()                              #�ǵ��ֶ��ر��ļ�

sys.stdout = temp                               #�ָ�Ĭ�������(�ն�)

print ('hey, i am back !')


print ('/tmp/test.txt:\n', open('/tmp/test.txt', 'r').read())
