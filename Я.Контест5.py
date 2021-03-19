kol = int(input())
array = list(map(int,input().split(" ")))
new_list = {}

for i in array:
	if i not in new_list:
		new_list[i] = 1

print(len(new_list))
