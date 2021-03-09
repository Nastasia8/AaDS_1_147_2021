a = int(input("a="))
b = int(input("b="))

def calc_for(a,b):
    summ = 0
    for i in range(a,b+1):
        if i%2 == 0:
            summ = summ + i
    print("Сумма=",summ)
def calc_while(a,b):
    summ = 0
    while a<b+1:
        if a%2 == 0:
            summ +=a
        a+=1
    print("Сумма=",summ)
calc_for(a,b)
calc_while(a,b)