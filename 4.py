def main(): 
     m = int(input("Введите число: "))
     

     print(funk(m))


def funk(zed):
     n=1
     if (zed >= 100000 and zed < 1000000):
        for i in range(0, 6):
            n *= zed % 10
            zed = zed // 10
        else:
            print("Ошибка")
        
     return n


main()
