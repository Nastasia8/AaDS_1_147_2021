num=[]
n = int(input())
for i in range(n):
    key,valve =map(int,input().split())
    num.append([key,valve])
for i in range(len(num)-1):
    for j in range(len(num)-i-1):
        if num[j][1] > num[j+1][1]:
            num[j], num[j+1] = num[j+1], num[j]
        elif num[j][1] == num[j+1][1]:
            if num[j][0] > num[j+1][0]:
                num[j], num[j+1] = num[j+1], num[j]
            
# for i in range(len(num)-1):
print(*num, sep=" ")