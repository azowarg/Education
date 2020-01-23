"""Write a Python program to count the number of characters (character frequency) in a string.
Sample String : google.com
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}"""

S = str(input("Enter string to count characters: "))
count = {i : S.count(x) for i in S}
print(count)
