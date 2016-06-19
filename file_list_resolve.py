#!/usr/bin/env python
#encoding=utf-8

# 也可以用列表解析, 一行代码就搞定

F = open('test.txt')

lines = F.readlines()
print ('\n\ntest1...\n\n', lines)



#也可以这样

[lines for lines in open('test.txt', 'r')]
print ('\n\ntest2...\n\n', lines)


lines = [line.rstrip().upper() for line in open('test.txt')]
print ("\n\nduang...\n\n", lines)



#()中的第一项是成员in测试, 返回True或False, 第二项打印前十个字或字符

lines = [('Just' in line, line[0:10]) for line in open('test.txt')]

print ("\n\nduang...duang...\n\n", lines)


#扩展的列表解析语法1
lines = [line.rstrip() for line in open('test.txt') if line[0:4] == "Just"]
print ("\n\nduang... * 3\n\n", lines)

#扩展的列表解析语法2
print ("\n\nduang... * 4\n\n", [x+y for x in '123' for y in 'abc'], "\n\n")
