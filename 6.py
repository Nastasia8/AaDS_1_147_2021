<<<<<<< HEAD

import math
n=int(input("Введите n: \n"))
s=0
k=0
def summ_chisel(k,s):
    while k<=n:
        k+=1
        f=math.factorial(k)
        s+=((-1)*k*((5-k)/f))
    print("Сумма=",round(s,3))
summ_chisel(k,s)                




=======
import math
n=int(input("Введите n: \n"))
s=0
k=0
def summ_chisel(k,s):
    while k<=n:
        k+=1
        f=math.factorial(k)
        s+=((-1)*k*((5-k)/f))
    print("Сумма=",round(s,3))
summ_chisel(k,s)                



>>>>>>> 34d0a67bca167cfb45d42ec6799ad4332d51d507
