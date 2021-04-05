from math import pi, sqrt

T = float(input("Введите T\n"))
m = float(input("Введите m\n"))
k = float(input("Введите k\n"))
def frequency(T):
    w = ((2 * pi)/T)
    print("frequency: {0:1.3f}".format(w))
def period(m,k):
    T = 2*pi*(sqrt(m/k))
    print("period: {0:1.3f}".format(T))
    
frequency(T)
period(m,k)