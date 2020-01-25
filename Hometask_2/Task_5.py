"""Написать программу, которая принимает от пользователя имя и пароль. Сравнивает пароль с заданным в коде.
В случае совпадения печатает в консоль "Password for user: <Имя пользователя> is correct"
Если пароль не совпадает, то печатает в консоль
"Password for user: <Имя пользователя> is incorrect"
"Please try again..."
И снова запрашивает пароль (не завершается).
"""

login_pas = {"azowarg": "1243Dr1", "kotletka": "955757", "firefighter": "burn12351"}
login = str(input('Username: ')).lower()
password = str(input("Password: "))
while password != login_pas[login]:
    print("Password for user:", login, "is incorrect \nPlease try again...")
    password = str(input("Password: "))
print("Good job!")
