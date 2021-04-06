S = str(input())
T = str(input())
k = 0
while k + len(T) <= len(S):
    if S[k:k + len(T)] == T:
        print(k, end = ' ')
    k = k + 1
