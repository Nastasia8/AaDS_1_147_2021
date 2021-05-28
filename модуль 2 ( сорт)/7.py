Arr = []
    length = int(input())

    for i in range(length):
        Arr.append(input())

    print("Initial array:")
    print(', '.join(Arr))
    Count = len(Arr[0])
    Phase=0
    for i in range(Count-1,-1,-1):
        Phase+=1
        print('**********')
        print("Phase",Phase)
        bucket = [[] for _ in range(10)]
        for j in range(len(Arr)):
            bucket[ord(Arr[j][i]) - ord('0')].append(Arr[j])
        for j in range(10):
            if len(bucket[j])==0:
                print(f'Bucket {j}: empty')
            else:
                print("Bucket "+str(j)+": ", end='')
                for now in range(len(bucket[j])-1):
                    print(bucket[j][now],end=', ')
                print(bucket[j][len(bucket[j])-1])
        p = 0
        for j in range(10):
            for k in range(len(bucket[j])):
                Arr[p] = bucket[j][k]
                p += 1

    print('**********')
    print("Sorted array:")

    print(', '.join(Arr))
