def calc_summ():
    summ = 0
    k = int(input("Введите k\n"))
    n = 1
    for i in range(1,k):
        summ = summ + (2/((2*n+1)*(2*n+3)))
        n = n + 1
    print("Сумма",summ)
def calc_comp():
    comp = 1
    k = int(input("Введите k\n"))
    n = 1
    for i in range(1,k):
        comp = comp*((-1)**(n-1)+n)
        n = n + 1
    print("Произведение",comp)
calc_summ()
calc_comp()

    