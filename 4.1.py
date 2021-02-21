# numbers =[1,-5,0,9,-17]
# print({number:"+" if number >0 else "-" if number<0 else "zero" for number in numbers})
def NOD(x, y):
    a = x
    b = y
    while x != 0 and y != 0:
        if x > y:
            x = x % y
        else:
            y = y % x

    print("NOD({0};{1}) = {2}".format(a, b, (x+y)))


x = int(input("x="))
y = int(input("y="))
NOD(x, y)
