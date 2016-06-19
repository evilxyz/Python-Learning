#!/usr/bin/env python
#encoding=utf-8

def kwonly(x, *y, z):       #出现在*args后面的参数必须以关键字传递!   z = 2
    print (x, y, z)

kwonly(1, 2, z=3)           # z is keyword-only 

kwonly(x=1, z=3)            # *y = ()   空元组

#kwonly(1, 2, 3)    这样会报错, 因为z没有以关键字形式时行赋值

######################## Advantage Test #########################

def kwonly(x, *, y, z):     # 星号后面代表后面的参数必须以keyword-only方式传递!(字典形式传递)
   print (x, y, z) 

kwonly(1, y=2, z=3)         #it's necessary

kwonly(z=3, y=2, x=1)       #倒序也可以

#kwonly(1, 2, 3)    it's wrong, because z, and y did not used keyword-only

####################### Deault values ##########################

def kwonly(x, *, y='evil', z):  #keyword-only对于带默认值的可以睁一只眼闭一只眼,但是对没有默认值的一率不让过!
    print (x, y, z)

kwonly(1, z=3)

kwonly(1, y='xyz', z=3)

#kwonly(1)           会报错

##################### *args 和 **args 之间的那点事 #############

def func(e, *v, i='i', **l):    # 1. *args必须写在**args前面, keyword-only必须写在*args之后, **args之前!
    print (e, v, i, l)          # 2. 如果它写到了*args之前,可以是默认位置参数, 而不是keyword-only

func(1, 2, i='i am i', l=3)

func(1, 2, 3, l=3, ll=3*3, lll = 3**3)

################### My Test ####################################

def func(e, v='v', *i, **l):    # v 是默认位置参数,非keyword-only
    print (e, v, i, l)

func(1, 2, 3, x=4)      # P461 wrong...

################## rule of function call #####################

def func(e, *v, i='i', **l):
    print (e, v, i, l)

func(1, *(2, 3), **{'i':'I', 'l':'L'})     # **{'i':'I', 'l':'L'}  等于 **dict(i='I', l='L')
                                           #可以把keyword-only 嵌入到**args调用中
                                           # *(2, 3) 和直接写2, 3 作用是一样的

func('E', 'V', 'I', 'L', **dict(x='X', y='Y', z='Z', i='-'))    #最后面dict,相当于把x, y, z 放到字典中



