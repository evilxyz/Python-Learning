#!/usr/bin/env python
#encoding=utf-8

R = range(3)
I = iter(R)

print (next(I)) #���һ��Ԫ��
print (next(I))
print (next(I))

II = iter(R)    #�����Ƿ�֧�ֶ��������

print (next(II))
print (next(II))

#�б����
print ('List Test')

L = [1, 2, 3, 4]
I1, I2 = iter(L), iter(L)

print (next(I1))
print (next(I2))

del L[2:]

print (next(I1))
print (next(I1))        #����ʾ StopInteration, �б�֧�ֶ�����������, ������һ����������з�ӳ���ǵ�ԭ���޸�
