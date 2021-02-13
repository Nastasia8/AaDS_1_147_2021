  from math import pi, sqrt
print ('jeskost')
k = float(input())
print('massa')
m = float(input())

def func_1(result):
    result = sqrt(k/m)
    return(result)

def func_2(result):
    result = 2*pi*sqrt(m/k)
    return(result)
print(round(func_1(0), 3))
print(round(func_2(0), 3))