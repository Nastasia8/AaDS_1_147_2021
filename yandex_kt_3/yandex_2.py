# Ошибка TL

def func(T, S):
    for i in range(len(S)+1):
        if S != T:
            S = S[-1:] + S[:-1]
        else:
            return(i)
    return('-1')

S = str(input())
T = str(input())
print(func(T, S))

