"""Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. 
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2"""

S = str(input("Enter strings separated by 'space': ")).split()
print(len([i for i in S if len(i) >= 3 and i[0] == i[len(i)-1]]))
