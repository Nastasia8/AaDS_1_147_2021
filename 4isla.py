print('summa')
x = float(input())
y = 15
z = 6
n = 1

def func(x, y, z, n):
    return round((x*((1+(y/100)/(z/12))**(z/(12*n)))), 3)
print(func(x, y, z, n))
