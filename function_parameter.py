#!/usr/bin/env python
#encoding=gbk

def f(L, S):
    L[0] = '����˧'
    S = 'test'

l = [1, 2, 3, 4, 'go', 'go', 'go']
s = 'evilxyz'   #��Ϊ���s��ȫ�ֱ���(��ģ�鶥������),��f�����ڵ�s����ͻ

f(l, s)         #�ɱ����ͨ��ָ�븳ֵ, ���ɱ����ͨ��"ֵ"����.
                #���,�ɱ������Ϊ����, �ں������޸Ļ�Ӱ���ⲿ����.
                #���ɱ������Ϊ����, �򲻻�Ӱ��

print (l, s)

############## ���������Ƿ�ɱ���� ################

def changer(L):
    L[0] = 'i can not change'

L = [1, 2]
changer(L[:])   #����ͨ�����ݿɱ����Ŀ���,�ﵽ�ں����ڲ����޸Ķ����Ŀ��

print (L)

############## other way

def changer1(L):
    L = L[:]    #���ڲ�ȥ����, ���ַ���Ӧ�ø�����!
    L[0] = 'i can not change'

changer1(L)
print (L)


############# other way

def changer2(L):
    L[0] = ['i can not change']

changer2(tuple(L))      #���ַ����ܼ���,�ᱨ��,��ΪԪ�鲻���Ըı�

print (L)

