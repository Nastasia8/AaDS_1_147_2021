x = int(input("Введите x: "))
y = int(input("Введите y: "))
z = int(input("Введите z: "))

D=y*y - 4*x*z

if D<0:
	print("корней нет")

if D==0:
	a=-y/2*x
	print(a)

if D>0:
	a1=(-y + D**0.5) / (2 * x)
	a2=(-y - D**0.5)/ (2 * x)
	print(a1,a2)
