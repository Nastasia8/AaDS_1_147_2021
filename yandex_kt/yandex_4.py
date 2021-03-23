def enter():
    N = int(input())
    if 1 <= N <= 100000:
        A = list(map(int, input().split(maxsplit = N - 1)))
        func(A)

def func(A):
    k = 0
    f = 1
    while f < int(len(A)):
        i = 0
        j = f
        while j < int(len(A)):
            if i < j and A[i] > A[j]:
                k = k + 1
            i = i + 1
            j = j + 1
        f = f + 1
    return(print(k))

enter()
