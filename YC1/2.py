n = int(input())
a = []
for i in range(n):
	a.append(list(map(int,input().split())))


a.sort(key = lambda x: x[0])
a.sort(key = lambda x: x[1], reverse = True)
for i in a:
	for b in i:
		print(b,end = ' ')
	print()


		
