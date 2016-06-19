#!/usr/bin/evn python
#encoding=utf-8

"""
self test
"""

def commas(N):
    """
    change N to digit groupings: xxx,yyy,zzz
    """

    digits = str(N)
    assert(digits.isdigit())    #if digits not digital, exit and alter
    result = ''

    while digits:
        digits, last3 = digits[:-3], digits[-3:]                    #circle get char, 
        result = (last3 + ',' + result) if result else last3        #good code! 

    return result

def money(N, width=0):
    """
    format number N for display with comas, 2 decimal digits,
    leading $ and sign, and optional padding: $ -xxx,yyy.zz
    """
    sign = '-' if N < 0 else ''
    N = abs(N)
    whole = commas(int(N))
    fract = '{0:.2f}'.format(N)[-2:]
    format_ = '{0}{1}.{2}'.format(sign, whole, fract)
    return '${0}'.format((width, format_))

if __name__ == '__main__':          #如何以顶层文件运行
    def selftest():
        tests = 0, 1
        tests += 12, 123, 1234, 12345, 123456, 1234567
        tests += 2 ** 32, 2 ** 100
        for test in tests:
            print (commas(test))

        print ('')
        tests = 0, 1, -1, 1.23, 1., 1.2, 3.14159
        tests += 12.34, 12.344, 12.345, 12.346
        tests += 1.2345, 1.2, 0.2345
        tests += -1.2345, -1.2, -0.2345
        tests += -(2 ** 32), -(2 ** 32 + .2345)
        tests += (2 ** 100), -(2 ** 100)
        for test in tests:
            print ('{0} [{1}]'.format(money(test, 17), test))
        
    import sys

    if len(sys.argv) == 1:
        selftest()
    else:
        print (money(float(sys.argv[1]), int(sys.argv[2])))

