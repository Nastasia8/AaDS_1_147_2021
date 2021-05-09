n = int(input())
nums = []
inteng = 10
for i in range(n):
    nums.append(input())
print('Initial array:')
print(', '.join(nums))
for i in range(len(str(max(nums)))):
    print('**********')
    print('Phase', i+1)
    buck = [[] for k in range(inteng)]
    for k in nums:
        f = int(k) // 10**i % 10
        buck[f].append(k)
    nums = []
    for k in range(inteng):
        nums = nums+buck[k]
        print('Bucket', k, end=": ")
        if len(buck[k]) == 0:
            print('empty')
        else:
            print(', '.join(map(str, buck[k])))
print('**********')
print('Sorted array:')
print(', '.join(map(str, nums)))