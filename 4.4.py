a = [[4, 3, 5, 1], [0, 7, 2, 9], [2, 6, 3, 8]]

print("Before:")
for num in range(len(a)):
    print(a[num])
print("After:")
for num in range(len(a)):
    print(a[num][::-1])

b = [[13, 97, 56], [17, 23, 85], [22, 45, 66]]

print("Before:")
for num in range(len(b)):
    print(b[num])
print("After:")
for num in range(len(b)):
    print(b[num][::-1])
