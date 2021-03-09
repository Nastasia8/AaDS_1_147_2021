import math
def func(k):
    summ = 0
    for i in range(1,k+1):
        summ+=((-1)i((5-i))/(math.factorial(i)))
    print("Сумма= {0:1.3f}".format(summ))
func(1)
