#!/usr/bin/env python
#encoding=utf-8

def maker(N):
    def action(X):
        return X ** N
    return action

F1 = maker(2)

print (F1(3))

F2 = maker(3)

print (F2(3))


#为什么可以这样咧, 实际上,在本地作用域内的N被作为执行状态信息保留了下来,我们返回其参数的平方运算.
#对工厂函数的每次调用都可得到一个自己的状态信息集合
