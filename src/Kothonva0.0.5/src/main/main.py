import random

def open(one , two):
    try:
        open(""+one+"",""+two+"")
    except:
        print("Error!")
def d(one , two):
    try:
        if str(two) == 'r':
            val = float(one) * 2
            return val
        elif str(two) == 'p':
            val = float(one) / 3.14
            return val
        else:
            print("Error")
    except:
        print("Error!")
def rsd(one):
    try:
        val = float(one) * float(one) * 3.14
        return val
    except:
        print("Error!")
def pai(one):
    try:
        val = float(one) * 2 * 3.14
        return val
    except:
        print("Error!")
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
        print("Error!")
def type(one):
    try:
        val = type(one)
        if str(val) == "<type 'int'>":
            return 0
        elif str(val) == "<type 'float'>":
            return 1
        elif str(val) == "<type 'str'>":
            return 2
        else:
            return val
    except:
        print("Error")
        e = 'Error'
        isi = isinstance(one)
        print(isi)
        return e
def isi(self , two):
    try:
        val = isinstance(self, two)
        return val
    except:
        self = 0
        two = 0
        return 'False'
