from math import pi, sqrt

def Period(k,m):
	T = 2*pi*sqrt(float(m)/float(k))
	print(round(T, 1))

def Frequency(k,m):
	w=sqrt(k/m)	
	print(round(w, 1))	

m = float(input("Введите массу груза:"))
k = float(input("Введите коэффициент жесткости пружины:"))
Period(k,m)	
Frequency(k,m)    




