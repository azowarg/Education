"""Написать функцию, которая принимает произвольное количество любых аргументов.
    Аргументами могут быть вложенные списки и кортежи, содержащие числа и другие списки и кортежи.
    Пример вызова функции: foo(1, 2, [3, 4, (5, 6, 0)], a=(10, 11), b=(3, 4, [5, 6, [7, 8], []]))
    Функция должна вернуть произведение и сумму всех ненулевых элементов вложенных чисел.
    Возможны циклические ссылки в аргументах. Пример такого аргумента: a = [1, 2, 3]; a.append(a)
    При обнаружении циклической ссылки нужно сообщить пользователю и вернуть None."""

"""Не реализовал поиск циклической ссылки, пробовал сделать это через модуль gc, но попытки не увенчались успехом"""
def sum_prod(*args, **kwargs):
    """Function returns sum and product of any number of arguments"""
    my_sum = 0
    my_product = 1
    all_args = list(args) + list(kwargs.values())

    def func(variable):
        for i in variable:
            if isinstance(i, (list, tuple)):
                func(i)
            elif i != 0:
                nonlocal my_sum
                my_sum += int(i)
                nonlocal my_product
                my_product *= int(i)
        return my_sum, my_product
    return print(func(all_args))


sum_prod(1, 2, [3, 4, (5, 6, 0)], a=(10, 11), b=(3, 4, [5, 6, [7, 8], []]))
