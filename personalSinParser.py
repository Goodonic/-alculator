import math
def psrp(formula_string):
    res = ''
    for i in str(formula_string):
        if i != 'p':
            res += i
        else:
            res += "math.pi"
    res = eval(res)

    #print(res)
    return res