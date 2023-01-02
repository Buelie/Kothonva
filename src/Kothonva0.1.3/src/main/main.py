import random
import json

def open(one , two):
    try:
        open(""+one+"",""+two+"")
    except:
        print("Error:Invalid Open With or non-existent file or duplicate name file or no permission to operate")
        return 404
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
    except TypeError:
        print("TypeError:Data type error")
        return 100
    except NameError:
        print("NameError:Naming error")
        return 101
    except ValueError:
        print("ValueError:The value is wrong")
        return 102
    except:
        print("Error:Unknown operation")
        return 404
def rsd(one):
    try:
        val = float(one) * float(one) * 3.14
        return val
    except TypeError:
        print("TypeError:Data type error")
        return 100
    except NameError:
        print("NameError:Naming error")
        return 101
    except ValueError:
        print("ValueError:The value is wrong")
        return 102
    except:
        print("Error:Unknown operation")
        return 404
def pai(one):
    try:
        val = float(one) * 2 * 3.14
        return val
    except:
        print("Error:Data that cannot be converted to float")
        return 404
def rec(one , two , three):
    try:
        if str(three) == 'c':
            val = sum([float(one),float(two)],0) * 2
            return val
        elif str(three) == 's':
            val = float(one) * float(two)
            return val
    except TypeError:
        print("TypeError:Data type error")
        return 100
    except NameError:
        print("NameError:Naming error")
        return 101
    except ValueError:
        print("ValueError:The value is wrong")
        return 102
    except:
        print("Error:Unknown operation")
        return 404
def add(one , two):
    try:
        val = float(one) + float(two)
        return val
    except TypeError:
        print("TypeError:Data type error")
        return 100
    except NameError:
        print("NameError:Naming error")
        return 101
    except ValueError:
        print("ValueError:The value is wrong")
        return 102
    except:
        print("Error:Unknown operation")
        return 404
def sub(one , two):
    try:
        val = one - two
        return val
    except TypeError:
        print("TypeError:Data type error")
        return 100
    except NameError:
        print("NameError:Naming error")
        return 101
    except ValueError:
        print("ValueError:The value is wrong")
        return 102
    except:
        print("Error:Unknown operation")
        return 404
def mul(one , two):
    try:
        val = one * two
        return val
    except TypeError:
        print("TypeError:Data type error")
        return 100
    except NameError:
        print("NameError:Naming error")
        return 101
    except ValueError:
        print("ValueError:The value is wrong")
        return 102
    except:
        print("Error:Unknown operation")
        return 404
def imt(self):
    try:
        __import__(''+self+'')
        return 0
    except TypeError:
        print("TypeError:Data type error")
        return 100
    except NameError:
        print("NameError:Naming error")
        return 101
    except ValueError:
        print("ValueError:The value is wrong")
        return 102
    except:
        print("Error:Unknown operation")
        return 404
def div(one , two):
    try:
        val = one / two
        return val
    except TypeError:
        print("TypeError:Data type error")
        return 100
    except NameError:
        print("NameError:Naming error")
        return 101
    except ValueError:
        print("ValueError:The value is wrong")
        return 102
    except:
        print("Error:Unknown operation")
        return 404
def choice(one):
    try:
        val = random.choice(one)
        return val
    except TypeError:
        print("TypeError:Data type error")
        return 100
    except NameError:
        print("NameError:Naming error")
        return 101
    except ValueError:
        print("ValueError:The value is wrong")
        return 102
    except:
        print("Error:Unknown operation")
        return 404
def randint(one , two):
    try:
        val = random.randint(one , two)
        return val
    except TypeError:
        print("TypeError:Data type error")
        return 100
    except NameError:
        print("NameError:Naming error")
        return 101
    except ValueError:
        print("ValueError:The value is wrong")
        return 102
    except:
        print("Error:Unknown operation")
        return 404
def evl(self):
    try:
        val = eval(self)
        return val
    except TypeError:
        print("TypeError:Data type error")
        return 100
    except NameError:
        print("NameError:Naming error")
        return 101
    except ValueError:
        print("ValueError:The value is wrong")
        return 102
    except:
        print("Error:Unknown operation")
        return 404
def rnd(one , two):
    try:
        val = round(one , two)
        return val
    except TypeError:
        print("TypeError:Data type error")
        return 100
    except NameError:
        print("NameError:Naming error")
        return 101
    except ValueError:
        print("ValueError:The value is wrong")
        return 102
    except:
        print("Error:Unknown operation")
        return 404
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
    except TypeError:
        print("TypeError:Data type error")
        return 100
    except NameError:
        print("NameError:Naming error")
        return 101
    except ValueError:
        print("ValueError:The value is wrong")
        return 102
    except:
        print("Error:Unknown operation")
        return 404
def isi(self , two):
    try:
        val = isinstance(self, two)
        return val
    except TypeError:
        print("TypeError:Data type error")
        return 100
    except NameError:
        print("NameError:Naming error")
        return 101
    except ValueError:
        print("ValueError:The value is wrong")
        return 102
    except:
        print("Error:Unknown operation")
        return 404
def cod(self):
    try:
        val = exec(""+self+"")
        print(val)
        return val
    except TypeError:
        print("TypeError:Data type error")
        return 100
    except NameError:
        print("NameError:Naming error")
        return 101
    except ValueError:
        print("ValueError:The value is wrong")
        return 102
    except:
        print("Error:Unknown operation")
        return 404
def asi(self):
    try:
        val = ascii(self)
        print("[asc]Value:"+val)
        return val
    except TypeError:
        print("TypeError:Data type error")
        return 100
    except NameError:
        print("NameError:Naming error")
        return 101
    except ValueError:
        print("ValueError:The value is wrong")
        return 102
    except:
        print("Error:Unknown operation")
        return 404
def itl(self):
    try:
        val = list(enumerate(self))
        return val
    except TypeError:
        print("TypeError:Data type error")
        return 100
    except NameError:
        print("NameError:Naming error")
        return 101
    except ValueError:
        print("ValueError:The value is wrong")
        return 102
    except:
        print("Error:Unknown operation")
        return 404
def id(self):
    try:
        val = id(self)
        return val
    except TypeError:
        print("TypeError:Data type error")
        return 100
    except NameError:
        print("NameError:Naming error")
        return 101
    except ValueError:
        print("ValueError:The value is wrong")
        return 102
    except:
        print("Error:Unknown operation")
        return 404
def hash(self):
    try:
        val = hash(self)
        return val
    except TypeError:
        print("TypeError:Data type error")
        return 100
    except NameError:
        print("NameError:Naming error")
        return 101
    except ValueError:
        print("ValueError:The value is wrong")
        return 102
    except:
        print("Error:Unknown operation")
        return 404
def len(self):
    try:
        val = len(self)
        return val
    except TypeError:
        print("TypeError:Data type error")
        return 100
    except NameError:
        print("NameError:Naming error")
        return 101
    except ValueError:
        print("ValueError:The value is wrong")
        return 102
    except:
        print("Error:Unknown operation")
        return 404
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
    except TypeError:
        print("TypeError:Data type error")
        return 100
    except NameError:
        print("NameError:Naming error")
        return 101
    except ValueError:
        print("ValueError:The value is wrong")
        return 102
    except:
        print("Error:Unknown operation")
        return 404
