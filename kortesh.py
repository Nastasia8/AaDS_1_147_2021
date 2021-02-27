x = (1, 2, 2, 3, 1, 2, 4, 3, 2, 2)
result = []
i = 0
y = 0

while i < len(x):
    if x[i] == 2:
        result.insert(y, i)
        y += 1
    i += 1
print(result)