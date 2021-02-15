ad = {1, 2, 3, 4, 5}


def counter(ad):
    summ = 0
    comp = 1
    for i in ad:
        summ += i
        comp *= i
    print('Сумма:', summ, '\nПроизведение:', comp)


counter(ad)
