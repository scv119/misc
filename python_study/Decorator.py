#!/bin/env python

def foo(callable):
    print '2'
    return callable

def decorator(i):
    def fun(callable):
        print i
        return callable
    return fun

@decorator('test')
def fun():
    print '1'

if __name__ == '__main__':
    fun()
    
