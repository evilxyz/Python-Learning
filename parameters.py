#!/usr/bin/env python
#encoding=utf-8

#���Ժ����������ݵ�ϸ��

#Ĭ�ϲ�������

def func(x, y='y', z='z'):  # y, z  is default parameter, if you call func(x) , y='y', z='z' , if you set y or z value, 
                                                                                # func(x, y='evil') , y='evil', z='z'
    print (x, y, z)

func('x ?\n', 'yes\n', 'it\'s me\n')

func(y='test y', x='i am x')            # match keywords, x='i am x', y='test y'


