import random

def add(one , two):
    try:
        val = float(one) + float(two)
        return val
    except:
        print("Error:Data that cannot be calculated or that cannot be transformed")
def sub(one , two):
    try:
        val = one - two
        return val
    except:
        print("Error:Data that cannot be calculated or that cannot be transformed")
def mul(one , two):
    try:
        val = one * two
        return val
    except:
        print("Error:Data that cannot be calculated or that cannot be transformed")
def div(one , two):
    try:
        val = one / two
        return val
    except:
        print("Error:Data that cannot be calculated or that cannot be transformed")
def choice(one):
    try:
        val = random.choice(one)
        return val
    except:
        print("Error: Data is suspected to be a list")
def randint(one , two):
    try:
        val = random.randint(one , two)
        return val
    except:
        print("Error:Data that cannot be randomly generated")
def evl(self):
    try:
        val = eval(self)
        return val
    except:
        print("Error:Unable to execute")
def rnd(one , two):
    try:
        val = round(one , two)
        cnt = 0
        while cnt <=2:
            cnt += 1
            ms = random.randint(1,10)
        return val
    except:
        pass
