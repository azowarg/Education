"""Write a Python program to find the highest 3 values in a dictionary"""

dict_1 = {}
print("Input Dictionary")
while True:
    i = str(input("Enter key & value separated by ':'. Leave the space empty to stop input \n"))
    if i == "":
        break
    i = i.split(":")
    dict_1[i[0]] = i[1]
S = list(dict_1.values())
print(*sorted(S, reverse=True)[:3])
