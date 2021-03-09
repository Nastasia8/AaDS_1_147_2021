<<<<<<< HEAD

import math

def function(x,y,z):
    d=int(pow(y,2)-4*x*z)
    x1=int()
    x2=int()
    if d==0:
        x1=(-y)/(2*x)
        print(x1)
    elif d < 0:
        print("Корней нет")
    else:
        x1=((-y)+math.sqrt(d))/(2*x)
        x2=((-y)-math.sqrt(d))/(2*x)
        print(x1)
        print(x2)
            
function(int(input("Введите значение a: ")),int(input("Введите значение b: ")),int(input("Введите значение c: ")))

=======
import math

def function(x,y,z):
    d=int(pow(y,2)-4*x*z)
    x1=int()
    x2=int()
    if d==0:
        x1=(-y)/(2*x)
        print(x1)
    elif d < 0:
        print("Корней нет")
    else:
        x1=((-y)+math.sqrt(d))/(2*x)
        x2=((-y)-math.sqrt(d))/(2*x)
        print(x1)
        print(x2)
            
function(int(input("Введите значение a: ")),int(input("Введите значение b: ")),int(input("Введите значение c: ")))


>>>>>>> 34d0a67bca167cfb45d42ec6799ad4332d51d507
