print("Введи числа для проверки")
a = int(input())
b = int(input())

while a != 0 and b != 0:
    
    if (a > b) and (a%b==0):
        a %= b
        sum = a + b
        print(sum)  
       
    if (a<b) and (b%a==0): #nteger division or modulo by zero надо как-то пофиксить
        b %= a
        sum = a + b
        print(sum)  

    else:
        print("нет общего делителя")
        break

      
       


