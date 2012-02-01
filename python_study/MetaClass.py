#!/bin/env python

class My_Meta_Class(type):
    def __init__(cls, name, bases, dct):
        print cls, bases
        super(My_Meta_class,cls).__init__(cls, name, bases, dct) 


class C(object):
    __meta_class__ = My_Meta_Class
    def __init__(self):
        pass


if __name__ == '__main__':
    c = C()
    C

