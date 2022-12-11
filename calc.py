from sin import sin
from cos import cos
from tg import tg
from ctg import ctg
import math

OPERATORS = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y),
             '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: x / y),
             's': (4, lambda x: sin(x)), 'c': (4, lambda x:cos(x)),
             't': (4, lambda x: tg(x)), 'C': (4, lambda x: ctg(x))}  # Числа - приоритет выполнения


def myEval(formula):
    def parse(formula_string):
        number = ''
        for s in formula_string:
            if s in '1234567890p.':  # Если символ цифра - собираем число
                number += s
            elif number:  # Если символ не цифра, то выдаём собранное число и начинаем собирать заново
                if number != 'p':
                    yield float(number)  # Если в конце строки есть число мы его выдаем
                else:
                    yield math.pi
                number = ''
            if s in OPERATORS or s in "()":  # Если символ  - оператор или скобка
                yield s
        if number:
            if number != 'p':
                yield float(number)  # Если в конце строки есть число мы его выдаем
            else:
                yield math.pi

    def shunting_yard(parsed_formula):
        stack = []
        for token in parsed_formula:
            # если элемент - оператор, то отправляем дальше все операторы из стека,
            # чей приоритет больше или равен пришедшему,
            # до открывающей скобки или опустошения стека.
            # здесь мы пользуемся тем, что все операторы право-ассоциативны
            if token in OPERATORS:
                while stack and stack[-1] != "(" and OPERATORS[token][0] <= OPERATORS[stack[-1]][0]:
                    yield stack.pop()
                stack.append(token)
            elif token == ")":
                # если элемент - закрывающая скобка, выдаём все элементы из стека, до открывающей скобки,
                # а открывающую скобку выкидываем из стека.
                while stack:
                    x = stack.pop()
                    if x == "(":
                        break
                    yield x
            elif token == "(":
                stack.append(token)
            else:
                yield token
        while stack:
            yield stack.pop()

    def calc(polish):
        stack = []
        for token in polish:
            if token in OPERATORS:
                if token != 'c' and token != 'C' and token != 's' and token != 't':
                    y, x = stack.pop(), stack.pop()
                    stack.append(OPERATORS[token][1](x, y))  # Вызываем функцию из списка операторов
                else:
                    x = stack.pop()
                    stack.append(OPERATORS[token][1](x))
            else:
                stack.append(token)

        return stack[0]  # Результат вычисления - единственный оставшийся обьект

    return calc(shunting_yard(parse(formula)))
