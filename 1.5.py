def Multiply(k=1):
    m = 1
    for n in range(1, k+1, 1):
        m *= (-1)**(n-1)+n
    return m


def Summa(k=0):
    s = 0
    for n in range(1, k+1, 1):
        s += 2/((2*n+1)*(2*n+3))
    return round(s, 4)


k = int(input("Enter a number:"))
print("Solution summa:", Summa(k))
print("Solution multiply:", Multiply(k))
