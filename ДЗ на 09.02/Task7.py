from math import sqrt

def sqEq(x,y,z):
    D = y * y - 4 * x * z
    if D < 0:
        return ("Корней нет.")
    if D == 0:
        return "X = " + str((-y) / (2 * x))
    if D > 0:        
        return "X1 = " + str(((-y)+sqrt(D))/2*x)+ "\nX2 = "+str(((-y)-sqrt(D))/2*x)

x = int(input("Укажите x: \n"))
y = int(input("Укажите y: \n"))
z = int(input("Укажите z: \n"))
print(sqEq(x,y,z))