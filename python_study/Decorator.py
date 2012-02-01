#!/bin/env python

def foo(callable):
    print '2'
    return callable

def decorator(i):
    def fun(callable):
        def dec_fun(*arg, **karg):
            g = callable(*arg, **karg)
            print dir(g)
            return g
        print i
        return dec_fun 
    return fun

@decorator('test')
def fun():
    print '1'

if __name__ == '__main__':
    fun()
    
