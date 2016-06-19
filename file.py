#!/usr/bin/env python
#encoding=utf-8

F = open('/tmp/myfile.txt', 'w')    #对文件进行写操作,如果没有则创建文件

F.write('i am first line\n')        #写入一行字符串, '\n'代表一行的结束

F.write('i am second line\n')

F.write('i am thread line\n')       #利用字符串逐行写入,也可以用列表一次写入

F.close()                           #关闭文件

F = open('/tmp/myfile.txt', 'r+')   #如果不加,默认是读文件,'r+'表示可读可写

print (F.read())                    #读取文件中的所有字符串, 如果加参数是读取之后的几个字节, 读取之后, 需要用seek方法来修改当前偏移量, 因为read后偏移量到了末尾

F.seek(0)                           #修改偏移量到文件头

print (F.read(5))                   #读取前5个字节的字符

print ('deadline', F.readline(2) + '\n')   #readline加参后读取之后的字符数

F.seek(0)

print (F.readline())                        #readline不加参直接读取一行

F.seek(50)

F.write('I am the last line !\n')          #写入字符串 

F.seek(0)

L = []
L = F.readlines()                          #读取所有内容到列表L, 是readlines, 后面有s

print (L)

L = ['123', 'abc']
F.writelines(L)                             #把列表字符串写入文件
F.seek(0)
print ('last:', F.read())

F.flush()
F.close()

for line in open('/tmp/myfile.txt'): print (line)


