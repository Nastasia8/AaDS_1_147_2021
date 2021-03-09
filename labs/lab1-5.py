k = int(input("Введите k\n"))

def calc_summ(k):
    summ = 0
    for n in range(1,k):
        summ +=(2/((2*n+1)*(2*n+3)))
        n = n + 1
    print("Сумма= {0:1.3f}".format(summ))
def calc_comp(k):
    comp = 1
    for n in range(1,k):
        comp *= ((-1)**(n-1)+n)
        n = n + 1
    print("Произведение",comp)
calc_summ(k)
calc_comp(k)
