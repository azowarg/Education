"""Write a Python script to merge two Python dictionaries"""

dict_1, dict_2 = {}, {}
i = 0
print("First Dictionary")
while True:
    i = str(input("Enter key & value separated by ':'. Leave the space empty to stop input \n"))
    if i == "":
        break
    i = i.split(":")
    dict_1[i[0]] = i[1]
print("Second Dictionary")
while True:
    i = str(input("Enter key & value separated by ':'. Leave the space empty to stop input \n"))
    if i == "":
        break
    i = i.split(":")
    dict_2[i[0]] = i[1]
dict_1.update(dict_2)
print("Union of dictionaries:\n", dict_1)
