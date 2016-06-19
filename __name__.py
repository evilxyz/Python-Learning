#!/usr/bin/env python
#encoding=utf-8

def tester():
    print ("running...")

if __name__ == '__main__':  #如果__name__ 等于 __main__ 代表正在以顶层文件执行,否则应该为模块导入
    tester()
else:
    print ('No, Don\'t do that')
