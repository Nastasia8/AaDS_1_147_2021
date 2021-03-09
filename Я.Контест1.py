v = int(input())
strok = input()
strok = strok.split(" ")
array=[]
for i in range(0,len(strok)):
	array.append(int(strok[i]))
m = len(strok)
num = 0
for i in range(0,m-1):
    for j in range(0,m-i-1):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]
            num+=1
            print(" ".join(map(str,array)))
if num==0:
    print(0)
