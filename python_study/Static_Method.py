#!/bin/env python
class A(object):
    count = 0
    @staticmethod
    def increase_count():
        A.count = A.count + 1
    @classmethod
    def increase_count2(cls):
        cls.count += 1
    @property
    def name(self):
        return '123'

