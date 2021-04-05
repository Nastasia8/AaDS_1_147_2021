a = [3, 8, 2, 1, 4, 7, 5, 6, 10, 9]
b = []
i = 0
for a[i] in range (1,11):
    if a[i]%2==0:
        b.append(a[i])
print(b)