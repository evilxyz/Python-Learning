#!/usr/bin/env python
#encoding=utf-8

x = 'evil.'
y = 'xyz'
z = 'It\'s me !'

if x:
    r = y
else:
    r = z

#����Ĵ���ܼ�,��д������... ��ʵ��py���и���Ԫ���ʽ, ����ʾ��

r = y if x else z   #��˼�������xΪ��, r = y, ���� r = z
