a = input('Input 1 number:')
b = input('Input 2 number:')

def HOD(a, b):    
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    print("HOD({0};{1}) = 2".format(a, b, (a + b)))
    


HOD(a, b)