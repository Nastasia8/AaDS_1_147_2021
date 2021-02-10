from math import pi, sqrt
def Period(k,m):
   T=2*pi*sqrt(float(m)/float(k))
   print("Period=",T)
   return(T)

def Frequency(T):
   w=(2*pi)/T
   print("Frequency=",w)

k=input("Enter k:")
m=input("Enter m:") 
T=Period(k,m)
Frequency(T)