import random

def GetGCD(x,y):
    while (x != 0 and y != 0):
        if x > y:
            x, y = y,x
        y -= x
        if y == 0:
            return x
def Task1():
    x = int(input("Введите X\n"))
    y = int(input("Введите Y\n"))
    print("НОД (",x,";",y,") = ",GetGCD(x,y))

def GetLCM(x,y):
    return x * y / GetGCD(x,y)

def Task2():
    x = int(input("Введите X\n"))
    y = int(input("Введите Y\n"))
    print("НОК (",x,";",y,") = ",GetNCD(x,y))

def numToOne(num):
    process = []
    while num > 1:
        if num % 2 == 0:
            num /= 2
        else:
            num*=3
            num += 1
            num /=2
        process.append(num)
    return process       

def Task3():
    num = int(input("Введите число:\n"))
    print(numToOne(num))


selection = int(input("Введите номер задания:\n"))
if selection == 1:
    Task1()
elif selection == 2:
    Task2()
elif selection == 2:
    Task2()
elif selection == 3:
    Task3()