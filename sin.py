import math
from personalSinParser import psrp

def sin(x):
    x = psrp(x)
    x %= math.pi
    print(x)
    i = 1
    lasts = 0
    s = x
    num = x
    sign = 1
    while s != lasts:
        lasts = s
        i += 2
        fact = math.factorial(i)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    return s

print('sin',sin('10*p/2'))