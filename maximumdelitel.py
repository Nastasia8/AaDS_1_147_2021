print('x')
x = int(input())
print('y')
y = int(input())
def func(x, y):
    ostatokDva = 1
    ostatokPerv = int(x % y)
    if ostatokPerv  > 0:
        ostatokDva = int(y % ostatokPerv)
        if ostTWO > 0:
            while ostatokDva > 0:
                ostatokPerv = int(ostatokPerv % ostatokDva)
                ostatokDva, ostatokPerv = ostatokPerv, ostatokDva
            return(ostatokPerv)
        else:
            return(ostatokPerv)  
    else:
        return(y)
      
if x < y:
    x, y = y, x
    print(func(x, y))
else:
    print(func(x, y))