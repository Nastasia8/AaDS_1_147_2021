print('4sila')
x = int(input())

def func(result):
    for i in str(x):
        result *= int(i)
    return(print(result))

if x > 99999 and x<1000000:
    func(1)
else:
    print('neto')
