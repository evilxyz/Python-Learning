#!/usr/bin/env python
#encoding=gb2312

#列表解析
#优点:C的速度, Py的精简

L = [1, 2, 3, 4, 5]

#列表中的每个元素+10
L = [x + 10 for x in L]   


#嵌套循环
res = [x + y for x in [1, 2, 3] for y in [100, 200, 300]] #相当于循环嵌套
print (res)

res = [(x, y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1]
print (res)


M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
N = [[2, 2, 2],
     [3, 3, 3],
     [4, 4, 4]]

#取出M中间一列
print ([row[1] for row in M])            
print ([M[row][1] for row in range(3)]) 

#对角线
print ([M[row][row] for row in range(3)]) 

#求M中所有和
print ('求M所有和:')
print (sum([sum(row) for row in M]))


#M,N矩阵相乘
print ('M',M, 'N', N)   # M[0][0] * N[0][0], M[0][1] * M[0][1]
print ([M[row][col] * N[row][col] for row in range(len(M)) for col in range(len(N))])  
print ('---')
# 生成[[], [], []] 形式的列表, col是外循环
print ([[M[row][col] * N[row][col] for row in range(len(M))] for col in range(len(N))])
print ('---')


#一个好玩的例子, 用多种方法去掉readlines()中的'\n'
F = open('/tmp/test', 'w')
F.write('i am good guy\ni want to be a security engineer\ni want to be richer\ni am a archer\n')
F.close()

print ([line[:-1] for line in open('/tmp/test')])               #显然列表解析比map要精简的多
print (list(map(lambda line: line[:-1], open('/tmp/test'))))    #map比for 快三倍
                            #line.rstrip()也可以
