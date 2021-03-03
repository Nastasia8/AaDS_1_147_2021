print('Введите x: ', end='')
x = int(input())
print('Введите y: ', end='')
y = int(input())

def func(x, y):
    ostTWO = 1
    ostONE = int(x % y)
    if ostONE > 0:
        ostTWO = int(y % ostONE)
        if ostTWO > 0:
            while ostTWO > 0:
                ostONE = int(ostONE % ostTWO)
                ostTWO, ostONE = ostONE, ostTWO
            return(ostONE)
        else:
            return(ostONE)  
    else:
        return(y)
      
if x < y:
    x, y = y, x
    print('НОД(', y, '; ', x, ') = ', func(x, y))
else:
    print('НОД(', x, '; ', y, ') = ', func(x, y))
