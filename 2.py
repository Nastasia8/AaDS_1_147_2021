#from math import pi, sqrt
##Text='Python is an interpreted, high-level and general-purpose programming language. Python\'s design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects. Python is dynamically-typed and garbage-collected.'.lower()
##print("p=",Text.count("p"),"o=",Text.count("o"))
#def Period(k,m):
#   T=2*pi*sqrt(float(m)/float(k))
#   print("Period=",T)
#   return(T)

#def Frequency(T):
#   w=(2*pi)/T
#   print("Frequency=",w)

#k=input("Enter k:")
#m=input("Enter m:") 
#T=Period(k,m)
#Frequency(T)

def summ(x,y):
    return x+y

def com(x,y):
    return x*y

def deff(x,y):
    if y==0:
        print("Ввод некорректных данных")
    return x/y

def minus(x,y):
    return x-y

def stepen(x,y):
    return x**y

x=float(input("Enter x:"))
y=float(input("Enter y:"))
z=int(input("Chose operation:"))

if z==1:
    print(summ(x,y))
elif z==2:
    print(com(x,y))
elif z==3:
    print(deff(x,y))
elif z==4:
    print(minus(x,y))
elif z==5:
    print(stepen(x,y))
