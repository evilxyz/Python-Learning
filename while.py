#!/usr/bin/env python
#encoding=gbk

'''
while True:
    reply = input('Enter text:')
    if reply == 'stop': break
    print (type(reply), reply.upper())         #input����Ĭ�Ϸ����ַ�������
'''

while True:
    reply = input('Enter Num:')
    
    if reply.isdigit():
        print (int(reply) ** 2)
    elif reply == 'stop' or reply == 'Stop' or reply == 'STOP':
        break
    else:
        print ('Error Input')
        
print ('Bye')
