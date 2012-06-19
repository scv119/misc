#!/bin/env python
class Account(object):
    num_account = 0
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        Account.num_account += 1

    def __del__(self):
        Account.num_account -= 1

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -+ amount

    def inquiry(self):
        return self.balance

class Evil_Account(Account):
    def __init__(self, name, balance, rate):
        super(Evil_Account,self).__init__(name,balance)
        self.rate = rate
        
