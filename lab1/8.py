def calc():
    C = 1
    number = input("Введите шестинзначное число\n")
    if len(number) == 6:
        for i in range(1,7):
            C = C*(int(number)%10)
            number = int(number)//10
    print(C)
calc()
