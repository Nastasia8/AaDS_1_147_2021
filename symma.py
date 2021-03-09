print('Kol-vo povtorov')
number = int(input())
result = 0

def proizveden(result, n):
    while n <= number:
        result *= (-1)**(n-1)+n
        n += 1
    return(result)

def summa(result, n):
    while n <= number:
        result += 2/((2*n+1)*(2*n+3))
        n += 1
    return(result)

print(round(proizveden(1, 1), 3))
print(round(summa(0, 1), 3))
