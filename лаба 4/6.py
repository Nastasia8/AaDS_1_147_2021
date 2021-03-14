spisok = [int(num) for num in input().split()]

def funk(numb):
    x = list()
    [x.append(num) for num in sorted(numb)]
    return tuple(x)

print(funk(spisok))