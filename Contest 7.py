"""
>>> import io, sys 
>>> sys.stdin = io.StringIO(chr(10).join(['9','12','32','45','67','98','29','61','35','09']))  # input
>>> Function()
Initial array:
12, 32, 45, 67, 98, 29, 61, 35, 09
**********
Phase 1
Bucket 0: empty
Bucket 1: 61
Bucket 2: 12, 32
Bucket 3: empty
Bucket 4: empty
Bucket 5: 45, 35
Bucket 6: empty
Bucket 7: 67
Bucket 8: 98
Bucket 9: 29, 09
**********
Phase 2
Bucket 0: 09
Bucket 1: 12
Bucket 2: 29
Bucket 3: 32, 35
Bucket 4: 45
Bucket 5: empty
Bucket 6: 61, 67
Bucket 7: empty
Bucket 8: empty
Bucket 9: 98
**********
Sorted array:
09, 12, 29, 32, 35, 45, 61, 67, 98
"""


def Function():
    n = int(input())
    lenth = 10
    Numbers = []
    arr_num = []
    for i in range(n):
        Numbers.append(input())
    for number in Numbers:
        arr_num.append(number)
    print('Initial array:')
    print(', '.join(Numbers))
    for i in range(len(Numbers[0])):
        print('**********')
        print('Phase', i+1)
        bucket = [[] for k in range(lenth)]
        for number in arr_num:
            bucket[int(number)//10**i % 10].append(number)
        arr_num = []
        for l in range(lenth):
            arr_num = arr_num+bucket[l]
            print('Bucket', l, end=": ")
            if len(bucket[l]) == 0:
                print('empty')
            else:
                print(', '.join(map(str, bucket[l])))
    print('**********')
    print('Sorted array:')
    print(', '.join(map(str, arr_num)))


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
