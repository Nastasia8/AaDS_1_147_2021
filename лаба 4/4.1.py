def main():
    print("Введи числа для проверки")
    a = int(input())
    b = int(input())
    gcd(a,b)

def gcd(two, one):
    while one != 0:
        (two, one) = (one, two % one)
    print(two)

main()   

      
       


