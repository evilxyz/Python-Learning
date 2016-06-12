#!/usr/bin/env python
#encoding=utf-8

#程序功能:输入choice, 输出字典中对应的价格

D = {'spam': 1.25, 
     'ham': 1.99, 
     'eggs':0.99, 
     'bacon': 1.10}

choice = input('Please Input Your Choice: ')

#实现 I
'''
if choice == 'spam':
    print (1.25)
elif choice == 'ham':
    print (1.99)
elif choice == 'eggs':
    print (0.99)
elif choice == 'bacon':
    print (1.10)
else:
    print ('No this Choice !')
'''

#实现 II
'''
print (D.get(choice, 'Bad Choice !'))
'''

#实现 IV
if choice in D:
    print (D[choice])
else:
    print ('Bad Choice !')
