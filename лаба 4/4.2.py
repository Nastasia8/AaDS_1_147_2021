import math
def main():
    print("Введите 2 числа для нахождения НОК")
    a = int(input())
    b = int(input())
    nok(a, b)
    nok1(a,b)

def nok(one, two):
    print("НОК:", one, two, "= ", ((one * two) // math.gcd(one, two)))
    
def nok1(a,b):
    m = a*b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    print("Нок вторым способом: ", m // (a+b))

main()        

    

    
      

