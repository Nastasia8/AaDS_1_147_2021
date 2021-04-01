a = int(input("Введите a : "))
b=0

def multiply(b, n):
    while n < a:
        b = b + 2/((2*n+1)*(2*n+3))
        n = n+ 1
    return(b)

def symma(b, n):
    while n < a:
        b = b * (-1)**(n-1)+n
        n = n + 1
    return(b)

print("Сумма числового ряда = ", round(multiply(1, 2), 3), "\n", "Произведение числового ряда = ", round(symma(1, 2), 3))