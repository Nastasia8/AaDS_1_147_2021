print('Введите степень y: ', end='')
y = float(input())
print('Введите степень z: ', end='')
z = float(input())
ps = list(range(1, 21))
i = 0

while i < len(ps):
    if ps[i] % 2 != 0:
        ps[i] = ps[i]**y**z
    i += 1

print('[', end='')
print(*ps, sep=', ', end='')
print(']')
