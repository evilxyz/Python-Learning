#!/usr/bin/env python
#coding=utf-8

import sys

s = 'Hex:{0:>10X}\nOct:{1:>10o}\nBin:{2:>10b}\n'.format(255, 255, 255)

# {0:>10X} ��ʾ��0������ 10���ַ���Ȳ����Ҷ���

print (s)




print ('My {1[spam]:<8} runs {0.platform:>8}'.format(sys, {'spam':'laptop'}))



data = dict(spam='laptop', platform=sys.platform)

print ('My {spam:<8} runs {platform:>8}'.format(**data))    #����0�˸��ַ�λ��,�����.  ����0 laptop, ����1 sys.platform




print ('{0:d}'.format(9999999999))
print ('{0:,d}'.format(9999999999))
print ('{0:,.2f}'.format(1234.567))                 #��λ�����ö��ŷָ�,��������λС��


print ('{} {} {} ?'.format('who', 'am', 'i'))       #Ҳ���Բ�������ƫ����
