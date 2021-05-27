def func():
    long = int(input())
    let = 10
    num = []
    arr = []
    for i in range(long):
        num.append(input())
    for number in num:
        arr.append(number)
    
    print('initial array:')
    print(', '.join(num))
    for i in range(len(num[0])):
        print('***')
        print('phase', i+1)
        buc = [[] for k in range(let)]
        for number in arr:
            buc[int(number)//10**i % 10].append(number)
        arr = []
        for g in range(let):
            arr = arr + buc[g]
            print('bucket', g, end=": ")
            if len(buc[g]) == 0:
                print('empty')
            else:
                print(', '.join(map(str, buc[g])))
    print('***')
    print('sorted array:')
    print(', '.join(map(str, arr)))
func()                