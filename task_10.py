i = 0
print('Введите степень x: ', end='')
y = float(input())
print('Введите степень y: ', end='')
z = float(input())
ps = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

while i < 19:
    if ps[i] % 2 != 0:
        ps[i] = ps[i]**(y**z)
    i += 1

print('[', end='')
print(*ps, sep=', ', end='')
print(']')
