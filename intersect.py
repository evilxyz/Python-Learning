#!/usr/bin/env python
#encoding=utf-8

def intersect(*args):
    res = []
    for x in args[0]:
        for arg in args[1:]:
            if x not in arg:
                break           # break 只是跳出本层循环
            else:
                res.append(x)
    return res


#print (intersect('evil', 'evab', 'vxyz'))   #多参会有bug...

def unique(*args):
    res = []
    for x in args[0]:
        for y in args[1:]:
            if x in y:
                break
            else:
                res.append(x)
    return res

#print (unique('evil', 'evab', 'vxyz'))



######################## 无BUG版 ###############################

def intersect(*args):       #找出第一个参数和后面的参数共有值
    res = []

    for x in args[0]:
        ok = True
        for y in args[1:]:
            if x not in y:
                ok = False
        if ok is True:
            res.append(x)
    return res

#print (intersect('evil', 'evab', 'vxyz'))

def unique(*args):          #第一个参数和后面的参数比对是否是惟一值
    res = []

    for x in args[0]:
        ok = False
        for y in args[1:]:
            if x in y:
                ok = True
        if ok is False:
            res.append(x)
    return res

#print (unique('evil', 'evab', 'vxyz'))
