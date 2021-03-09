n=int(input())

arr=[]
for i in range(n):
    arr.append(input())

print (*arr,sep = ", ")

print("Initial array:")

print(', '.join(arr))


count = len(arr[0])
phase=0
rang=10
for i in range(count-1,-1,-1):
    phase+=1
    print('**********')
    print(f'Phase {phase}')
    bucket = [[] for _ in range(rang)]
    for j in range(len(arr)):
        bucket[ord(arr[j][i]) - ord('0')].append(arr[j])
    for j in range(rang):
        if len(bucket[j])==0:
            print(f'Bucket {j}: empty')
        else:
            print("Bucket "+str(j)+": ", end='')
            for now in range(len(bucket[j])-1):
                print(bucket[j][now],end=', ')
            print(bucket[j][len(bucket[j])-1])
    p = 0
    for j in range(rang):
        for k in range(len(bucket[j])):
            arr[p] = bucket[j][k]
            p += 1

print('**********')
print("Sorted array:")

print(', '.join(arr))