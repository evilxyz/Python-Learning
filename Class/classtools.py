#!/usr/bin/env python
#encoding=utf-8

class AttrDisplay:
    """
    Provides an inheritable print overload method that displays
    instances with their class names and a name=vlaue pair for
    each attribute stored on the instance itself (but not attrs
    inherited from its classed). Can be mixed into any class, 
    and will work on any instance.
    """

    def gatherAtters(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('{0} {1}'.format(key, getattr(self, key))) #self.__dict__[key]  is ok
        return ', '.join(attrs)                                     #build a string from sequence(list or tuple)
    
    def __str__(self):
        return '{0:<10} {1}'.format(self.__class__.__name__, self.gatherAtters())
                                    # display father class name

if __name__ == '__main__':
    class TopTest(AttrDisplay):
        count = 0                       # class attribute !!!
        def __init__(self):
            self.attr1 = TopTest.count  # instance attribute !!!
            self.attr2 = TopTest.count + 1
            TopTest.count += 2
            # print(self.__dict__)

    class SubTest(TopTest):
        pass



    X, Y = TopTest(), SubTest()

    print ('X => ', X)
    print ('Y => ', Y)

