a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))
t=0

for x in range(a,b):
	if x%2==0:   
		t=t+x
print("сумма чётных чисел: ",t)


while a<=b:
	if a%2==0:
		t=t+a
		a+=1
	else:
		a+=1
print("сумма чётных чисел: ",t)
