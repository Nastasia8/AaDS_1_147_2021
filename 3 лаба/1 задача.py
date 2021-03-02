
import math
def sum(k):
    sum = 0
    for n in range(1,k+1):
        sum+=((-1)*k*((5-k))/(math.factorial(k)))
    print("Сумма= {0:1.3f}".format(sum))
sum(1)