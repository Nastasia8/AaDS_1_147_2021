print ('Введите символ: ', end='')
x = int(input())

def func(kor, x):
    if x in kor:
        i = 0
        while i <= len(kor):
            if kor[i] == x:
                break
            i += 1
        j = -1
        while j >= -len(kor):
            if kor[j] == x:
                if i != len(kor) + j:
                    print(kor[i:len(kor) + j + 1])
                    break
                else:
                    print(kor[i:])
            j -= 1
    else:
        print('В кортеже отсутствует данный элемент')

func((1, 2, 3, 4, 5, 4, 6, 2, 4, 7, 9, 4, 5, 6, 5, 0, 4, 2), x)

