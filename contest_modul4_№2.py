l = int(input())
s = list(map(int, input().split()))

tup = [0]
tr2 = [0]

for i in range(l):
	while tup[-1] == tr2[-1] + 1:
		tr2.append(tup[-1])
		tup.pop()
	if s[i] == tr2[-1] + 1:
		tr2.append(s[i])
	else:
		tup.append(s[i])

while tup[-1] == tr2[-1] + 1:
	tr2.append(tup[-1])
	tup.pop()

if tr2[-1] == l:
	print('YES')
else:
	print('NO')