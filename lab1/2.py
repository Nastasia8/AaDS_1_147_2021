from math import pi, sqrt
def main():
    T = float(input("Введите T\n"))
    frequency(T)
    m = float(input("Введите m\n"))
    k = float(input("Введите k\n"))
    period(m,k)


def frequency(T):
    
    w = ((2 * pi)/T)
    print(w)
def period(m,k):
  
    T = 2*pi*(sqrt(m/k))
    print(T)
    
main()     
