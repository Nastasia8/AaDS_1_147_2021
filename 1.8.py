def pro(k=0):
    n = 1
    if(k >= 100000 and k < 1000000):
        for i in range(0, 6):
            n *= k % 10
            k = k // 10
    else:
        print("Error")
    return n


k = int(input("Enter a number:"))
print(pro(k))
