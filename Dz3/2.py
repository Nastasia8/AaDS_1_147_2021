def f(i):
    if(i == 0):
        return 0
    elif(i == 1):
        return 3
    else:
        return f(i-1) + f(i-2)
    
for i in range (0,16):
    print(f(i))

    