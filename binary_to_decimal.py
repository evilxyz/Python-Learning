#!/usr/bin/python

import sys


i = 0

b = sys.argv[-1]

print (type(b))
print (b)

while b != '':
    i = i * 2 + ord(b[0])-ord('0')
    b = b[1:]

print (i)
