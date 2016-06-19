#!/usr/bin/env python
#encoding=utf-8

import sys
import getopt

def usage():
    print ('usage...')
    print('getopt_test.py -v -o /home --help www.baidu.com')

def main():
    try:
        # 选项会进入opts, 参数会放入 args,      短格式后面想要有参数需要加':'
        opts, args = getopt.getopt(sys.argv[1:], "ho:v", ["help", "output="])   # 长格式后面有等号代表后面还有参数
        print(opts, args)

    except getopt.GetoptError as err:
        print (err)
        usage()
        sys.exit(2)
    
    output = None
    verbose = False
    
    for o, a in opts:
        if o == "-v":
            verbose = True
            print (verbose)
        elif o in ('-h', '--help'):
            usage()
            sys.exit()
        elif o in ('-o', '--output'):
            output = a
            print (a)
        else:
            assert False, 'unhandled option'

if __name__ == "__main__":
    main()
