a = int(input())
array = list(map(int,input().split(" ")))
st = {}

for i in array:
	if i not in st:
		st[i] = 1

print(len(st))
