n = int(input('Введите число: '))
mult = 1
d = n
k = 1
while d // 10 > 0:
    k += 1
    d = d // 10
if k == 6:
    while n > 0:
        digit = n % 10
        mult = mult * digit
        n = n // 10
    print("Произведение:", mult)
print("Количество цифр:", k)
if k != 6:
    print("Ошибка")
22
