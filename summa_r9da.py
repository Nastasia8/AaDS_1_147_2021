import math
def func(k):
    summ = 0
    for i in range(1,k+1):
        summ+=((-1)*k*((5-k))/(math.factorial(k)))
    print("Сумма= {0:1.3f}".format(summ))
func(1)