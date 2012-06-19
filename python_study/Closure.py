#!/bin/env python

def count_down(n):
    a_list = [n]
    def next():
        a_list[0] = a_list[0] - 1
        return a_list[0]

    return next

if __name__ == '__main__':
    next = count_down(10)
    while True:
        i = next()
        if i < 0:
            break
        print i
