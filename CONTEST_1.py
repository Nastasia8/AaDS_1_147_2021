def sort(a):
    b = 0
    for i in range(N-1):
        for j in range(N-i-1):
            if a[j] > a[j+1]:
                b = a[j]
                a[j] = a[j+1]
                a[j+1] = b
                b +=1
                print(' '.join(map(str, a)))
    if b == 0:
        return(print(0))
N = int(input())
a = list(map(int,input().split()))[:N]
sort(a)