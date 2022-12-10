import math
from radianParser import radianParser
from sin import sin
from cos import cos

def tg(x):
    try:
        res = sin(x) / cos(x)
        return res
    except:
        print("Недопустимое значение функции")

#print('tg',tg('11*p/2'))