#!/usr/bin/env python
#encoding=gb2312

#�б����
#�ŵ�:C���ٶ�, Py�ľ���

L = [1, 2, 3, 4, 5]

#�б��е�ÿ��Ԫ��+10
L = [x + 10 for x in L]   


#Ƕ��ѭ��
res = [x + y for x in [1, 2, 3] for y in [100, 200, 300]] #�൱��ѭ��Ƕ��
print (res)

res = [(x, y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1]
print (res)


M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
N = [[2, 2, 2],
     [3, 3, 3],
     [4, 4, 4]]

#ȡ��M�м�һ��
print ([row[1] for row in M])            
print ([M[row][1] for row in range(3)]) 

#�Խ���
print ([M[row][row] for row in range(3)]) 

#��M�����к�
print ('��M���к�:')
print (sum([sum(row) for row in M]))


#M,N�������
print ('M',M, 'N', N)   # M[0][0] * N[0][0], M[0][1] * M[0][1]
print ([M[row][col] * N[row][col] for row in range(len(M)) for col in range(len(N))])  
print ('---')
# ����[[], [], []] ��ʽ���б�, col����ѭ��
print ([[M[row][col] * N[row][col] for row in range(len(M))] for col in range(len(N))])
print ('---')


#һ�����������, �ö��ַ���ȥ��readlines()�е�'\n'
F = open('/tmp/test', 'w')
F.write('i am good guy\ni want to be a security engineer\ni want to be richer\ni am a archer\n')
F.close()

print ([line[:-1] for line in open('/tmp/test')])               #��Ȼ�б������mapҪ����Ķ�
print (list(map(lambda line: line[:-1], open('/tmp/test'))))    #map��for ������
                            #line.rstrip()Ҳ����
