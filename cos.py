import math
from radianParser import radianParser


def cos(x):
    x = radianParser(x)
    i = 0
    if x > 2 * math.pi:
        x = x % (2 * math.pi)
    # if x == math.pi / 2:
    #     return 0

    lasts = 0
    s = 1
    num = 1
    pm = 1
    while s != lasts:
        lasts = s
        i += 2
        fact = math.factorial(i)
        num *= x ** 2
        pm *= -1
        s += num / fact * pm
        return round(s)

#print('cos',cos('30'))