"""Написать свою имплементацию функции range() из Python 2.x (аналогично Python 3, только возвращает список)"""


def my_range(*args):
    if len(args) == 1:
        start = 0
        stop = args[0] - 1
        step = 1
    elif len(args) == 2:
        start = args[0]
        stop = args[1] - 1
        step = 1
    elif len(args) == 3:
        start = args[0]
        stop = args[1] - 1
        step = args[2]
    else:
        return "Incorrect number of arguments"
    var_list = [start]
    while start < stop:
        start += step
        var_list.append(start)
    return var_list
    