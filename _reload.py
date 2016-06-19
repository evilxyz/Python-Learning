#!/usr/bin/env python
#encoding=utf-8

#使用reload需要导入imp, imp.reload

import time
import imp
import _re


if __name__ == '__main__':

    '''
        在程序输出的过程中, 更改_re模块中的test函数输出内容, 会发现更改后自动输出新内容.
    '''

    while True:
        _re.test()
        imp.reload(_re)
        time.sleep(1)
