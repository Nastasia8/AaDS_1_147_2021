def Sum(k):
    sum = 0.0
    for n in (range(1,k+1)):
        sum+=(2 / (2 * n + 1) * (2 * n + 3))
    return sum

def Mult(k):
    res = 1.0
    for n in (range(1,k+1)):
        res*=((-1) ** (n - 1) + n)
    return res


k = int(input("Введите k: "))
Sum(k)
Mult(k)
return