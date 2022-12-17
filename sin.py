import math
from radianParser import radianParser

def sin(x):
    x = radianParser(x)
    x %= math.pi*2
    #print(x)
    i = 1
    lasts = 0
    s = x
    num = x
    pm = 1
    while s != lasts:
        lasts = s
        i += 2
        fact = math.factorial(i)
        num *= x * x
        pm *= -1
        s += num / fact * sign
    return round(s)

#print('sin',sin('10*p/2'))