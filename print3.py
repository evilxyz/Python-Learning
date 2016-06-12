#!/usr/bin/env python
#encoding=utf-8

import sys

###################### ��ͨʵ�ְ� ###############################

def print3(*args, **kargs):
    sep = kargs.get('sep', ' ')          #��������ʽ��**kargsȡ������, ������ʱû�и�sep��ֵ, ��sep = ' '
    end = kargs.get('end', '\n')         #ͬ��, ���û��end��ֵ, end='\n'
    file=kargs.get('file', sys.stdout)   #�����
    output = ''
    first = True
    
    for arg in args:
        output += ('' if first else sep) + str(arg)     #������, �ж��Ƿ��ǵ�һ�ν���ѭ��,�����,�򷵻�'', ���򷵻�sep
        first = False
    file.write(output + end)

###################### keyword-only ʵ�ְ� #######################

def print30(*args, sep=' ', end='\n', file=sys.stdout):
    output = ''
    first = True

    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False

    file.write(output + end)

#���û���Ŵ��ܵ�

##################### ���쳣�� #####################################

def print300(*args, **kargs):
    sep = kargs.pop('sep', ' ')
    end = kargs.pop('end', '\n')
    file = kargs.pop('file', sys.stdout)
    if kargs: raise TypeError('extra keywords: %s' % kargs)
    output = ''
    first = True

    for arg in args:
        output += ('' if first else sep)+arg
        first = False
    file.write(output + end)

