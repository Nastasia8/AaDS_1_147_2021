from math import pi, sqrt

def period(mass, fr):
    return 2*pi*sqrt(mass/fr)
def cikl(m,k):
    return sqrt(k/m)
m=int(input())
k=int(input())
print("period = {0:1.3f}".format(period(m,k)))
print("cikl = {0:1.3f}".format(cikl(m,k)))

