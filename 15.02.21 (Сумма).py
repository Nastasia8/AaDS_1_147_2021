print ('Введите  N:')
n=float(input())
def summa(n):
    k=1
    sum=0
    while k<=n:
        sum +=(-1)*k*((5-k)/factorial(k))
        k+=1
    return (sum)
def factorial(k):
    if k>1:
        return k*factorial(k-1)
    return (k)
print (round(summa(n),2))
