#!/bin/env python
from contextlib import contextmanager
class Context_Manager(object):
    def __init__(self, a_list):
        self.the_list = a_list
        self.working_copy = list(self.the_list)

    def __enter__(self):
        return self.working_copy

    def __exit__(self, type, value, tb):
        if type is None:
            self.the_list[:] = self.working_copy
        return False

@contextmanager
def fun_context_manager(a_list):
    working_copy = list(a_list)
    yield working_copy
    a_list[:] = working_copy

if __name__ == '__main__':
    x = range(0,10)
    with Context_Manager(x) as working_copy:
        working_copy.append(1)
        working_copy.append(2)
    print x 

    try:
        with Context_Manager(x) as working_copy:
            working_copy.append(3)
            raise Exception('')
    except Exception as e:
        pass

    print x

    x = range(0,10)
    with fun_context_manager(x) as working_copy:
        working_copy.append(1)
        working_copy.append(2)
    print x 

    try:
        with fun_context_manager(x) as working_copy:
            working_copy.append(3)
            raise Exception('')
    except Exception as e:
        pass

    print x
