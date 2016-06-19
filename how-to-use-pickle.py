#!/usr/bin/env python
#encoding=utf-8

import pickle

def usePickle():

    D = {'x': 1, 'y': 2, 'z': 3}
    
    F = open('/tmp/test.txt', 'wb')
    
    pickle.dump(D, F)
    
    F.close()
    
    F1 = open('/tmp/test.txt', 'rb')
    
    print (pickle.load(F1))
    
    F1.close()

if __name__ == '__main__':
    usePickle()
