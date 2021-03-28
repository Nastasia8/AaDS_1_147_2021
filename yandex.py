#sort 1
N = int(input())
numbers = [int(i) for i in input().split()][:N]

check = 0

for i in range(N-1):
    for j in range(N-i-1):
	    if numbers[j] > numbers[j+1]:
		    numbers[j],numbers[j+1] = numbers[j+1],numbers[j]
		    print(" ".join(map(str, numbers)))
		    check = 1
    
if check == 0:
	print(0)
	
#sort 2
N = int(input())
a = []

for i in range(N):
    a.append([int(j) for j in input().split()][:N])

for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        if a[j+1][1] > a[j][1]:
            a[j+1],a[j] = a[j],a[j+1]

for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        if a[j+1][1] == a[j][1]:
            if a[j+1][0] < a[j][0]:
                a[j+1],a[j] = a[j],a[j+1]

for i in range(len(a)):
    print(*a[i])
