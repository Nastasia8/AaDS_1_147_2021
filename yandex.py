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