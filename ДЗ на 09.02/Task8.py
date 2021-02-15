def sixdig(number):
    result = 1
    if len(number) == 6:
         for i in number:
             result *= int(i)
    else:
        return ("Длина чимла не равна шести")
    return result

number = input("Введите число.\n")
print(sixdig(number))