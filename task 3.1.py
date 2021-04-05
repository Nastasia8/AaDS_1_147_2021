import math

def main():
    
    cul(1)

def cul(k):
    sum = 0
    for n in  range(1, k+1):
        sum+=((-1)*k*(5-k))/(math.factorial(k))
    print("равно = ",sum )

main()
