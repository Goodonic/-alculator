import math
from radianParser import radianParser
from sin import sin
from cos import cos

def ctg(x):
    try:
        res = cos(x) / sin(x)
        return res
    except:
        print("Недопустимое значение функции")

#print('ctg',ctg('0'))