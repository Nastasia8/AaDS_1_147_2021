from math import pi, sqrt
def main():
    T = float(input("Введите T\n"))
    frequency(T)
    m = float(input("Введите m\n"))
    k = float(input("Введите k\n"))
    period(m,k)


def frequency(T):
    if T==0:
        print("error(T = 0)")
    else:
         w = ((2 * pi)/T)
         print(w)
   
def period(m,k):
    if k==0:
        print("error(k = 0)")
    else:
         T = 2*pi*(sqrt(m/k))
         print(T)   
  
    
    
main()     
