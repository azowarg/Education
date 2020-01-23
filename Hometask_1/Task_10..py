"""Write a Python program to get the difference between the two lists"""

S_1 = input("Enter elements of first list separated by 'space': ").split()
S_2 = input("Enter elements of second list separated by 'space': ").split()
print(set(S_1).symmetric_difference(set(S_2)))
