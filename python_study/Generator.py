#!/bin/env python
def count_down(n):
    while n > 0:
        yield n
        n = n - 1

if __name__ == '__main__':
    for i in count_down(10):
        print i

    x = count_down(10)
    print x.next()
    print x.next()
    x.close()
    print x.next()
