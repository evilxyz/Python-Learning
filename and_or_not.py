#!/usr/bin/env python
#encoding=utf-8

# and , or ���᷵�� True��False, �᷵�����������е�һ��.

# or ��ִ�ж�·����. (����߶���Ϊ��֮��Ͳ����ж��ұ߶���)
# and��ִ�ж�·����, (����߶���Ϊ��֮��Ͳ����ж��ұ߶���

x = 'evil'
y = 'xyz'
z = None

print (x and y) #�᷵��y����
print (x or y) #�᷵��x����

print ({} and []) #�᷵��{} , �����{}ΪFalse��,ֱ�ӷ���{}
print ({} or [])  #�᷵��[], �����{}ΪFalse��,�����������[]�Ƿ�ΪTrue, ��[]Ҳ��False, �򷵻� []

