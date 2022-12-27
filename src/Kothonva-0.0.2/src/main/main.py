import random
import _thread

class cal:
    def __init__(self , one , two):
        self.one = one
        self.two = two
    def add(self):
        try:
            val = self.one + self.two
            return val
        except (TypeError,KeyError,ValueError,AttributeError,AssertionError,ArithmeticError):
            print("Error:Cannot be calculated")
    def sub(self):
        try:
            val = self.one - self.two
            return val
        except (TypeError,KeyError,ValueError,AttributeError,AssertionError,ArithmeticError):
            print("Error:Cannot be calculated")
    def mul(self):
        try:
            val = self.one * self.two
            return val
        except (TypeError,KeyError,ValueError,AttributeError,AssertionError,ArithmeticError):
            print("Error:Cannot be calculated")
    def div(self):
        try:
            val = self.one / self.two
            return val
        except (TypeError,KeyError,ValueError,AttributeError,AssertionError,ArithmeticError):
            print("Error:Cannot be calculated")
class random:
    def __init__(self , one , two):
        self.one = one
        self.two = two
    def choice(self):
        try:
            val = random.choice(self.one)
            return val
        except  (TypeError,KeyError,ValueError,AttributeError,AssertionError,ArithmeticError):
            print("Error:Random generation failed")
    def randint(self):
        try:
            val = random.randint(int(self.one),int(self.two))
            return val
        except  (TypeError,KeyError,ValueError,AttributeError,AssertionError,ArithmeticError):
            print("Error:Random generation failed")
class type:
    def __init__(self , one):
        self.one = one
    def val(self):
        try:
            val = type(self.one)
            return val
        except  (TypeError,KeyError,ValueError,AttributeError,AssertionError,ArithmeticError):
            print("Error:The type could not be detected")
def tha(one , two , three , four):
    try:
        _thread.start_new_thread(one)
        _thread.start_new_thread(two)
        _thread.start_new_thread(three)
        _thread.start_new_thread(four)
    except:
        print("Error:Thread startup failed")
