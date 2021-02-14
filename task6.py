def main():
    funk()



def funk():
    diction = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    sum = 0
    proiz = 1
    for i in diction:
        sum += i
        proiz *= i
    print("Сумма: ", sum, " Произведение: " , proiz)

main()