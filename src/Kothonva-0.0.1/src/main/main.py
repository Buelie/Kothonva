import random

class cal:
    def __init__(self , one , two):
        self.one = float(one)
        self.two = float(two)
    def add(self):
        val = self.one + self.two
        return val
    def sub(self):
        val = self.one - self.two
        return val
    def mul(self):
        val = self.one * self.two
        return val
    def div(self):
        val = self.one / self.two
        return val
class random:
    def __init__(self , one , two):
        self.one = one
        self.two = two
    def choice(self):
        val = random.choice(self.one)
        return val
    def randint(self):
        val = random.randint(int(self.one),int(self.two))
        return val
