"""You are given with 3 sets, find if third set is a subset of the first and the second sets
Input: set([1,2]), set([2,3), set([2])
Expected result: True
Input: set([1,2]), set([3,4), set([5])
Expected result: False"""

set_1 = set(input("Input elements of first set separated by space: ").split())
set_2 = set(input("Input elements of second set separated by space: ").split())
set_3 = set(input("Input elements of third set separated by space: ").split())
set_3.issubset(set_1) and set_3.issubset(set_2)
