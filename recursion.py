#!/usr/bin/env python
#encoding=utf-8

def mysum(L):
    print (L)
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])      #Call myself

print (mysum([1, 2, 3, 4, 5]))

def mysum(L):
    return 0 if not L else L[0] + mysum(L[1:])

def mysum(L):
    return L[0] if len(L) == 1 else L[0] + mysum(L[1:])




def mysum(L):
    first, *rest = L    #first=L[0], rest=L[1:]
    print (first, rest, L)
    return first if not rest else first + mysum(rest)

print (mysum([1, 2, 3, 4, 5]))
print (mysum(['e', 'v', 'i', 'l']))
"""
1 [2, 3, 4, 5] [1, 2, 3, 4, 5]
2 [3, 4, 5] [2, 3, 4, 5]
3 [4, 5] [3, 4, 5]
4 [5] [4, 5]
5 [] [5]
15
"""
