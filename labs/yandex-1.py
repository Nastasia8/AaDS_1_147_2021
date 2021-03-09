def sort(a):
    s = 0
    for i in range(X-1):
        for j in range(X-i-1):
            if a[j] > a[j+1]:
                b = a[j]
                a[j] = a[j+1]
                a[j+1] = b
                s +=1
                print(' '.join(map(str, a)))
    if swap == 0:
        return(print(0))
X = int(input())
a = list(map(int,input().split()))[:s]
s(a)