v = int(input()) #кол-во элементов массива
strok = input() #ввод чисел
strok = strok.split(" ")
array=[]
for i in range(0,len(strok)): #заполняем массив из строки
	array.append(int(strok[i]))
m = len(strok)
num = 0
for i in range(0,m-1):
    for j in range(0,m-i-1):
        if array[j] > array[j+1]:#если элементы идут не в том порядке, то переставляем их
            array[j], array[j+1] = array[j+1], array[j] 
            num+=1 #увеличивается кол-во перестановок
            print(" ".join(map(str,array))) #вывод через пробел
if num==0: #не было перестановок
    print(0)