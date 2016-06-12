#!/usr/bin/env python
#encoding=utf-8

# and , or 不会返回 True和False, 会返回两个对象中的一个.

# or 会执行短路运算. (即左边对象为真之后就不再判断右边对象)
# and会执行短路运算, (即左边对象为假之后就不再判断右边对象

x = 'evil'
y = 'xyz'
z = None

print (x and y) #会返回y对象
print (x or y) #会返回x对象

print ({} and []) #会返回{} , 检测完{}为False后,直接返回{}
print ({} or [])  #会返回[], 检测完{}为False后,还会继续测试[]是否为True, 若[]也是False, 则返回 []

