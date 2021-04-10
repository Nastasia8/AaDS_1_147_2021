def func(S, T):
    arr = [0] * len(S)
    l = r = 0 
    for i in range(1, len(S)):
        if i <= r:
            arr[i] = min(arr[i-l], r-i+1)
        while arr[i]+i < len(S) and S[arr[i]] == S[arr[i]+i]:
            arr[i] += 1
        if arr[i]+i-1 > r:
            l = i
            r = arr[i] + i - 1
    for i in range(len(arr)):
        if arr[i] == len(T):
            print (i-len(T)-1, end=' ')

S = str(input()) 
T = str(input()) 
S = T + '&' + S 
func(S, T) 
