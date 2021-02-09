from math import pi, sqrt

def frequency():
    T = float(input("Введите T\n"))
    w = ((2 * pi)/T)
    print(w)
def period():
    m = float(input("Введите m\n"))
    k = float(input("Введите k\n"))
    T = 2*pi*(sqrt(m/k))
    print(T)
    
frequency()
period()