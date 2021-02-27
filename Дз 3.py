#3.1
print('Введите колличество повторений: ')
n = int(input())
res = 0
def fac(k):
if k == 0:
return 1
return fac(k-1) * k
def func_1(res, k):
while k < n:
res += (-1)*k*((5-k)/(fac(k)))
k += 1
return(res)

print('Сумма = ', round(func_1(0, 1), 2))
#3.4
spis = ('Bass', 'Pike', 'Roach', 'Catfish', 'Trout', 'Mackerel', 'Salmon', 'Zander', 'Anchovy')
print(spis)

spis = sorted(spis)
print(spis)

for i in spis:
        print(i[-1:])
#3.5
list = [14, 46, 10, -78, 0, 6, -31, -24, 56, 17, -83, -4]

for i in list:
    if i > 0:
        print('positive:', i)
    elif i < 0:
        print('negative:', i)
    else:
        print('zero:', i)

ad = ([{'14': 'positive',
         '46': 'positive',
         '10': 'positive',
         '-78': 'negative',
         '0': 'zero',
         '6': 'positive',
         '-31': 'negative',
         '-24': 'negative',
         '56': 'positive',
         '17': 'positive',
         '-83': 'negative',
         '-4': 'negative'
         }])

print(ad)
