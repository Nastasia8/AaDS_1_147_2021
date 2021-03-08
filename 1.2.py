from math import pi, sqrt


def Period(k, m):
    if float(k) != 0:
        T = 2*pi*sqrt(float(m)/float(k))
        print("Period=", round(T, 4))
        return(T)


def Frequency(T):
    if T != None:
        w = (2*pi)/T
        print("Frequency=", round(w, 4))


k = input("Enter k:")
m = input("Enter m:")
T = Period(k, m)
Frequency(T)
