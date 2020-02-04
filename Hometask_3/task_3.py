"""Написать функцию, которая будет принимать только 4 позиционных аргументы (все аргументы числовые).
    Функция должна вернуть среднее арифметическое аргументов и самый большой аргумент за все время вызовов этой функции.
    Пример: foo(1,2,3,4) -> 2.5, 4
                  foo(-3, -2, 10, 1) -> 1.5, 10
                  foo(7,8,8,1) -> 6, 10"""

def four_numbers(var_1, var_2, var_3, var_4):
    srednee_arifmet = (var_1 + var_2 + var_3 + var_4)/4
    maximum = max([var_1, var_2,  var_3, var_4])
    def inner(maximum):
        return maximum
    return srednee_arifmet, inner()

four_numbers(1, 2, 3, 4)
four_numbers(-3, -2, 10, 1)
four_numbers(7,8,8,1)