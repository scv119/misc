#!/bin/env python


def dec(coroutine):
    def func(*arg, **kargs):
        g = coroutine(*arg, **kargs)
        g.next()
        return g
    return func
    
@dec
def coroutine():
    n = None
    while True:
        n = (yield)
        print n

if __name__ == '__main__':
    a = coroutine()
    a.send(1)
    a.send(2)
