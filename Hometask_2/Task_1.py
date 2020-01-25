"""Написать функцию, которая печатает квадраты всех нечетных чисел в произвольном интервале [0, Х]. А так же количество
 таких чисел."""


def seq_square(x):
    var = [i**2 for i in range(x + 1) if i % 2]
    return print("Numbers:", *var, "\nNumber of numbers:", len(var))
