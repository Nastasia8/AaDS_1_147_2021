print ('Введите x: ', end='')
x = float(input())
print('Введите y: ', end='')
y = float(input())
print('Введите операцию (+, -, *, /, **): ', end='')
oper = input()
if (oper == '+'):
    print('x + y = ', x+y)
elif (oper == '-'):
    print('x - y = ', x-y)
elif (oper == '*'):
    print('x * y = ', x*y)
elif (oper == "/"):
    if (y == 0):
        print('Sorry, на 0 нельзя') 
    else:
        print('x / y = ', x/y)
elif (oper == '**'):
    print('x**y = ', x**y)
else:
    print('Неверная операция')
