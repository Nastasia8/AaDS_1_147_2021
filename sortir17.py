#задача1
m = int(input())
arr = [int(num) for num in input().split()]
p = True

for i in range(m-1):
	for j in range(m-1-i):
		if arr[j] > arr[j+1]:
			arr[j],arr[j+1]=arr[j+1],arr[j]
			p = False
			for l in range(m):
				print(arr[l], end = " ")
if p==True:
	print(0)



#задача2
n=int(input())
matrix=[]
for i in range(n):
    key,value= map(int,input().split())
    matrix.append([key,value])

for i in range(n-1):
    for j in range(n-1-i):
        if matrix[j][1] < matrix[j+1][1]:
            matrix[j], matrix[j+1] = matrix[j+1], matrix[j]
        if matrix[j][1] == matrix[j+1][1] and matrix[j][0] > matrix[j+1][0]:
            matrix[j], matrix[j+1] = matrix[j+1], matrix[j]

[print(i[0], i[1]) for i in matrix]



#задача5
b={}
n=int(input())
stri=input()
mas=stri.split()
for a in mas:
    b[int(a)]=1
print(len(b))



#задача6
sklad=int(input())
prod=list(map(int,input().split()))
zakaz=int(input())
plus=list(map(int,input().split()))
num=[0]*(sklad+1)

for now in plus:
    num[now]+=1

for i in range(sklad):
    if prod[i]<num[i+1]:
        print("yes")
    else:
        print("no")