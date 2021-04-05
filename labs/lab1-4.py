def calc(m):
    i = 15
    p = 100000
    n = 10
    s=p*(1+((i/100)/(m/12))**(m/(12*n)))
    print(s)

calc(3)
calc(6)
calc(12)