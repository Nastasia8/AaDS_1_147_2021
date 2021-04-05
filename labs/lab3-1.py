import math
def calc_summ(k):
    summ = 0
    for n in range(1,k+1):
        summ+=((-1)*k*((5-k))/(math.factorial(k)))
    print("Сумма= {0:1.3f}".format(summ))
calc_summ(1) 