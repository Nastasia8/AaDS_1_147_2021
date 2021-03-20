n = int(input())
a = list(map(int,input().split()))[:n]
	
sorts = 1
passes = 0
while sorts != 0:
	sorts = 0
	for i in range(len(a) - 1):
		if a[i] > a[i + 1]:
			a[i], a[i + 1] = a[i + 1],a[i]
			for b in range(len(a)):
				print(a[b], end = ' ')
			print()
			sorts+=1
			passes +=1
	if (sorts == 0 and passes == 0):
			print(0)
		