def Summa(P=1000, n=12, m=12):
    I = 15
    S = 0
    if m == 12:
        S = P*(1+I/100)**n
    elif m == 3 or m == 6:
        S = P*(1+(I/100)/(m/12))**(n*m/12)
    else:
        return ("Error")
    return round(S, 2)


P = float(input("Введите сумму для рассчёта:"))
n = float(input("Введите количество лет:"))
m = float(input("Введите период начисления процентов 12, 6, 3 месяцев:"))
print(Summa(m=m, P=P, n=n))
