import random
import json

def open(one , two):
    try:
        open(""+one+"",""+two+"")
    except:
        print("Error:Invalid Open With or non-existent file or duplicate name file or no permission to operate")
def d(one , two):
    try:
        if str(two) == 'r':
            val = float(one) * 2
            return val
        elif str(two) == 'p':
            val = float(one) / 3.14
            return val
        else:
            print("Error:Data that cannot be converted to float or a mode that does not exist")
    except:
        print("Error:Unknown operation")
def rsd(one):
    try:
        val = float(one) * float(one) * 3.14
        return val
    except:
        print("Error:Data that cannot be converted to float")
def pai(one):
    try:
        val = float(one) * 2 * 3.14
        return val
    except:
        print("Error:Data that cannot be converted to float")
def rec(one , two , three):
    try:
        if str(three) == 'c':
            val = sum([float(one),float(two)],0) * 2
            return val
        elif str(three) == 's':
            val = float(one) * float(two)
            return val
    except:
        print("Error:Data that cannot be converted to float")
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
def imt(self):
    try:
        __import__(''+self+'')
        return 0
    except:
        print("Error:A library does not exist or failed to import a library")
        return 'error'
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
        return val
    except:
        print("Error:Wrong data or execution error")
def tpe(one):
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
        print("Error:The type of data that cannot be judged")
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
def cod(self):
    try:
        val = exec(""+self+"")
        print(val)
        return val
    except:
        print("Error:Non-executable code")
def asi(self):
    try:
        val = ascii(self)
        print("[asc]Value:"+val)
        return val
    except:
        print("Error:Data that could not be transformed")
def itl(self):
    try:
        val = list(enumerate(self))
        return val
    except:
        print("Error:An error occurred in the run")
def id(self):
    try:
        val = id(self)
        return val
    except:
        return 'error'
def hash(self):
    try:
        val = hash(self)
        return val
    except:
        return 'error'
def len(self):
    try:
        val = len(self)
        return val
    except:
        print('Error')
        return 'error'
def json(self , two):
    try:
        if str(two) == 'dump':
            val = json.dumps(self)
            return val
        elif str(two) == 'loads':
            val = json.loads(self)
            return val
        else:
            print("This not is a effective value")
    except:
        print("Error:Unable to parse JSON or unable to write JSON")
        return 'error'
