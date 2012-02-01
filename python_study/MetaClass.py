#!/bin/env python
alist = []

class MetaClass(type):
    def __new__(meta, classname, bases, classDict):
        alist.append(meta)
        print 'Class Name:', classname
        print 'Bases:', bases
        print 'Class Attributes', classDict
        classDict['method1'] = classDict['method'] 
        return super(MetaClass, meta).__new__(meta, classname, bases, classDict)


    def __init__(cls, classname, bases, classDict):
        alist.append(cls)
        print('wtf')
        cls.method2 = classDict['method1']
        super(MetaClass, cls).__init__(classname, bases, classDict)

class Test(object):
    __metaclass__ = MetaClass
    def __init__(self):
        pass

    def __new__(cls):
        return object.__new__(cls)

    def method(self):
        pass

if __name__ == '__main__':
    print dir(Test)
    test = Test()
    test.method1()
    print alist
    print test.__init__
    print Test.__new__
    

