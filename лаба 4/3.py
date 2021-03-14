def main():

    funk()

def funk():
    slv = []
    x = int(input("Введите натуральное число\n"))
    while x!=1:
        if x%2 == 0:
            x = x/2
            slv.append(int(x))
        else:
            x = (((x*3)+1)/2)
            slv.append(int(x))
    print(slv)

main()