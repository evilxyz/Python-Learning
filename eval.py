#!/usr/bin/env python
#encoding=utf-8

x, y, z = 3, 4, 5
S = 'I am a string'
L = [11, 12, 13]
D = {'x':9, 'y':10, 'z':11}

F = open('/tmp/test.txt', 'w')

F.write(S + '\n')                        #���ļ�д���ַ���
F.write('%s,%s,%s\n' % (x, y, z))        #��int����ת��str����д���ļ�
F.write(str(L) + '$' + str(D) + '\n')    #���б���ֵ�ת���ַ���д��

F.close()

for line in open('/tmp/test.txt'):
    print (line, end='')                 #�������

F = open('/tmp/test.txt', 'r')

S1 = F.readline()
print (S1.rstrip())                      #ȥ�س����ո�

line = F.readline()
line = line.split(',')                  #��ȡ3,4,5����','�и����б�

L1 = [int(num) for num in line]             #���б��е�ÿһ��ת����int����
print (L1)

line = F.readline()

parts = line.split('$')

objects = [eval(P) for P in parts]

print (objects)
