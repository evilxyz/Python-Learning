#!/usr/bin/env python
#encoding=utf-8

()                      #��Ԫ��
T = (0,)                #����һ��Ԫ�ص�Ԫ��
T = (0, 'Ni', 1.2, 3)   #��Ԫ��Ԫ��
T = 0, 'Ni', 1.2, 3     #��������Ҳ����Ŷ, �����Ƽ�

T = ('abc', ('def', 'ghi')) #Ƕ��Ԫ��

print (T[0])
print (T[1][1])             #Ԫ�������

T2 = ('i am xyz', 18, 'man')

print ('T + T2 =', T+T2)    #�ϲ�
print ('T * 3 =', T*3)      #�ظ�
print ('T[1:3] =', T[1:3])  #��Ƭ

T = tuple('spam')           #һ���ɵ�����������Ԫ��

for x in T: print (x)       #����

print ('len', len(T))       #Ԫ�鳤��

print ('spam in T', 'spam' in T)    #��Ա��ϵ

T = tuple(x + 2 for x in range(10, 15))

print (T)

T = tuple(x * 2 for x in [2, 4, 6, 8])   #��������Ԫ��
print (T)

T = T+(12, 13, 14, 15)

print ('T.index(12)', T.index(12))       #����
print ('T.count(12)', T.count(12))       #ͳ��

T = (1, [2, 3], 4)

T[1][0] = 'I can changed'           #Ԫ������������б���ֵ�,��ô���Ըı�
                                    #���ɱ���ֻ������Ԫ�鱾����,������������
print (T)
