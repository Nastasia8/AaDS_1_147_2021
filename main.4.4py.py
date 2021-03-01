m = [[4, 3, 5, 1], [0, 7, 2, 9], [2, 6, 3, 8]]


def diag(m):
    print("1. Matrix before conversion")
    for i in range(len(m)):
        print(m[i])
    print('1. Matrix after conversion')
    for i in range(len(m)):
        print(m[i][::-1])


diag(m)

n = [[13, 97, 56], [17, 23, 85], [22, 45, 66]]


def diag(n):
    print("2. Matrix before conversion")
    for i in range(len(n)):
        print(n[i])
    print('2. Matrix after conversion')
    for i in range(len(n)):
        print(n[i][::-1])


diag(n)