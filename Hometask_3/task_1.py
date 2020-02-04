"""Написать несколько функций, которые в качестве единственного
      аргумента принимают список (или кортеж) целых чисел.
- первая функция должна вернуть квадраты элементов коллекции;
- вторая функция должна вернуть только элементы на четных позициях;
- третья функция возвращает кубы четных элементов на нечетных позициях."""


def squares(collection):
    """Returns squares of all elements of the collection"""
    return print(*[i**2 for i in collection
                   if isinstance(collection, (list, tuple))])


def elem_even(collection):
    """Returns elements on even position"""
    return print(*[i for i in collection[1::2]
                   if isinstance(collection, (list, tuple))])


def odd_to_cube(collection):
    """Returns cubes of even elements on odd position"""
    return print(*[i**3 for i in collection[::2]
                   if isinstance(collection, (list, tuple)) and i % 2 == 0])