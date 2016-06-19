#!/usr/bin/env python
#encoding=utf-8

def kwonly(x, *y, z):       #������*args����Ĳ��������Թؼ��ִ���!   z = 2
    print (x, y, z)

kwonly(1, 2, z=3)           # z is keyword-only 

kwonly(x=1, z=3)            # *y = ()   ��Ԫ��

#kwonly(1, 2, 3)    �����ᱨ��, ��Ϊzû���Թؼ�����ʽʱ�и�ֵ

######################## Advantage Test #########################

def kwonly(x, *, y, z):     # �Ǻź���������Ĳ���������keyword-only��ʽ����!(�ֵ���ʽ����)
   print (x, y, z) 

kwonly(1, y=2, z=3)         #it's necessary

kwonly(z=3, y=2, x=1)       #����Ҳ����

#kwonly(1, 2, 3)    it's wrong, because z, and y did not used keyword-only

####################### Deault values ##########################

def kwonly(x, *, y='evil', z):  #keyword-only���ڴ�Ĭ��ֵ�Ŀ�����һֻ�۱�һֻ��,���Ƕ�û��Ĭ��ֵ��һ�ʲ��ù�!
    print (x, y, z)

kwonly(1, z=3)

kwonly(1, y='xyz', z=3)

#kwonly(1)           �ᱨ��

##################### *args �� **args ֮����ǵ��� #############

def func(e, *v, i='i', **l):    # 1. *args����д��**argsǰ��, keyword-only����д��*args֮��, **args֮ǰ!
    print (e, v, i, l)          # 2. �����д����*args֮ǰ,������Ĭ��λ�ò���, ������keyword-only

func(1, 2, i='i am i', l=3)

func(1, 2, 3, l=3, ll=3*3, lll = 3**3)

################### My Test ####################################

def func(e, v='v', *i, **l):    # v ��Ĭ��λ�ò���,��keyword-only
    print (e, v, i, l)

func(1, 2, 3, x=4)      # P461 wrong...

################## rule of function call #####################

def func(e, *v, i='i', **l):
    print (e, v, i, l)

func(1, *(2, 3), **{'i':'I', 'l':'L'})     # **{'i':'I', 'l':'L'}  ���� **dict(i='I', l='L')
                                           #���԰�keyword-only Ƕ�뵽**args������
                                           # *(2, 3) ��ֱ��д2, 3 ������һ����

func('E', 'V', 'I', 'L', **dict(x='X', y='Y', z='Z', i='-'))    #�����dict,�൱�ڰ�x, y, z �ŵ��ֵ���



