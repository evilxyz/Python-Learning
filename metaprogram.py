#!/usr/bin/env python
#encoding=utf-8

#Ԫ�������

"""
metaprogram.py: a module that lists the namespaces of other modules
"""

seplen = 60
sepchr = '-'

def listing(module, verbose=True):
    sepline = sepchr * seplen
    if verbose:
        print (sepline)
        print ('name:', module.__name__, 'file:', module.__file__)
        print (sepline)

    count = 0
    for attr in module.__dict__:
        print ('{0:02d}) {1}'.format(count, attr), end=' ')
        if attr.startswith('__'):                #���attr�����ú���, �ж�ǰ�����ַ��Ƿ�Ϊ__, Ҳ����attr[0:2] == '__'
            print ('<build-in name>')
        else:
            print (getattr(module, attr))
            
        count += 1    

    if verbose:
        print (sepline)
        print (module.__name__, 'has {0:d} names'.format(count))
        print (sepline)


if __name__ == '__main__':          #������Զ����ļ����еĻ�
    import metaprogram              #�����Ե����Լ�..
    listing(metaprogram)
