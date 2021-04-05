def main():
    a = [[1, 2, 3], [6, 7, 8], [9, 11, 12]]
    funk(a)

def funk(a):
    print("Матрица изначальная")
    for i in range(len(a)):
        print(a[i])
    for i in range(len(a)):
        a[i][-i-1] *= 2
    print('Матрица после')
    for i in range(len(a)):
        print(a[i])

main()