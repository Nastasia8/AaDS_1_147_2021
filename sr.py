print ('vvedite')
x = int(input())

def func(lol, x):
    if x in lol:
        i = 0
        while i <= len(lol):
            if lol[i] == x:
                break
            i += 1
        y = -1
        while j >= -len(lol):
            if lol[y] == x:
                if i != len(lol) + j:
                    print(lol[i:len(lol) + y + 1])
                    break
                else:
                    print(lol[i:])
            y -= 1
    else:
        print('error')

func((1, 2, 3, 4, 5, 4, 6, 2, 4, 7, 9, 4, 5, 6, 5, 0, 4, 2), x)