"""Написать функцию вычисления факториала числа"""


def factorial(x):
    var = 1
    for i in range(2, x + 1):
        var *= i
    return var
