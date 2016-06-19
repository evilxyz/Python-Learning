#!/usr/bin/env python
#encoding=utf-8

class Squares:
    def __init__(self, start, stop):            #save state when created
        self.value = start - 1
        self.stop = stop
        
    def __iter__(self):                         #get iterator object on iter
        return self

    def __next__(self):                         #return a square on each iteration
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value
#        return self.value ** 2


if __name__ == '__main__':
    s = Squares(1, 5)

    for i in s:
        print (i)
    
