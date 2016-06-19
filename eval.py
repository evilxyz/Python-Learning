#!/usr/bin/env python
#encoding=utf-8

x, y, z = 3, 4, 5
S = 'I am a string'
L = [11, 12, 13]
D = {'x':9, 'y':10, 'z':11}

F = open('/tmp/test.txt', 'w')

F.write(S + '\n')                        #向文件写入字符串
F.write('%s,%s,%s\n' % (x, y, z))        #把int类型转成str继续写入文件
F.write(str(L) + '$' + str(D) + '\n')    #把列表和字典转成字符串写入

F.close()

for line in open('/tmp/test.txt'):
    print (line, end='')                 #迭代输出

F = open('/tmp/test.txt', 'r')

S1 = F.readline()
print (S1.rstrip())                      #去回车及空格

line = F.readline()
line = line.split(',')                  #读取3,4,5后用','切割变成列表

L1 = [int(num) for num in line]             #把列表中的每一项转换成int类型
print (L1)

line = F.readline()

parts = line.split('$')

objects = [eval(P) for P in parts]

print (objects)
