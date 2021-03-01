ans = []
def calc():
    a = int(input("Введите натуральное число\n"))
    while a!=1:
        if a%2 == 0:
            a = a/2
            ans.append(int(a))
        else:
            a = (((a*3)+1)/2)
            ans.append(int(a))
    print(ans)
calc()