spis = '14, 46, 10, -78, 0, 6, -31, -24, 56, 17, -83, -4'.split(', ')
itog = ''
n = 0

while n < len(spis):
    if int(spis[n]) > 0:
        itog += 'positive '
    elif int(spis[n]) < 0:
        itog += 'negative '
    else:
        itog += 'zero '
    n += 1

itog = itog.split(' ')
itog = dict(zip(spis, itog))

print(itog)
