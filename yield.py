#!/usr/bin/env python
#encoding=utf-8

def gensquars(N):   #����������,֧�ֵ�����Э��
    for i in range(N):
        yield i**2  #ÿִ��һ��,����Ȩ��Ҫ��������

for i in gensquars(5):
    print ('==>', i)

x = gensquars(4)    #x������һ���ɵ����Ķ���
print ('x ==>', x)  #�õ���һ������������,֧�ֵ�����Э��(��__next__ ����)

print (next(x))     #��x.__next__() ��һ����Ч��
print (next(x))

########### ��չ������ send , next
print ('---------- send, next -----------')

def gen():
    for i in range(10):
        x = yield i
        print (x)

G = gen()

print (G.__next__())        #��ͬ��next(G), ����G.send(value)֮ǰ,����next(G)����ʼһ��������
print (G.send(20))          #G.send(20) ��20���͸�������G , ����x = 20
                            #����G.send(20)��,��ָ��������Ĵ���.
#print (G.send(99))
print (G.__next__())        #�᷵��һ��None, Ϊʲô ?
