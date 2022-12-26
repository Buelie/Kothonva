import random
import logging

class syst:
    def __init__(self , ner):
        self.ner = ner
    def print(self):
        print(str(self.ner))
        return 0
class add:
    def __init__(self , one , two):
        self.one = one
        self.two = two
    def cont(self):
        val = self.one + self.two
        print("log : cont(add) is"+val)
        return val
class sub:
    def __init__(self , one , two):
        self.one = one
        self.two = two
    def cont(self):
        val = self.one - self.two
        print("log : cont(sub) is"+val)
        return val
class mul:
    def __init__(self , one , two):
        self.one = one
        self.two = two
    def cont(self):
        val = self.one * self.two
        print("log : cont(mul) is"+val)
        return val
class random:
    def __init__(self , one , two):
        self.one = one
        self.two = two
    def choice(self):
        val = random.choice(self.one)
        print("log : random choice >"+val)
        return val
    def randint(self):
        val = random.randint(self.one , self.two)
        print("log : random randint >"+val)
        return val
class classes:
    def __init__(self , one , two):
        self.one = one
        self.two = two
    def add(self):
        name = self.one
        print("creat a class >"+name)
    def dele(self):
        name = self.one
        del name
