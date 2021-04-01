x = int(input("Введите x: "))
y = int(input("Введите y: "))

print ("выберите операцию из списка:\n","сложение-1\n", "умножение-2\n","деление-3\n","вычитание-4\n","возведение в степень-5\n")

n=int(input("Введите номер операции: "))

if n==1 :
    print("x+y=", x+y)

if n==2:
    print("x*y=",x*y)

if n==3:
    if y==0:
        print('nooooooooooo')
    elif y!=0:
        print("x\y=", x/y) 
if n==4:
    print("x-y=", x-y)

if n==5:
    print('X в степени y =', x**y)
    