a = [7, 1, 3, 4, 3, 9, 14, -5, -17, -13, -19, -18]
def calc():
    i = -1
    s = 0
    while a[i] < 0:
        s+=a[i]
        i-=1
    print(s)
calc()