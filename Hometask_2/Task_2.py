"""Написать функцию, которая принимает 3 числа (a,b,c) и проверяет сколько чисел между ‘a’ и ‘b’ делятся на ‘c’"""


def trinity(a, b, c):
    var = [i for i in range(a, b + 1) if i % c == 0]
    return print("Numbers", *var, "can be divided by", c, "\nNumber of numbers: ", len(var))
