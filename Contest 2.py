num=[]
n = int(input())
for i in range(n):
    key,valve =map(int,input().split())
    num.append([key,valve])
for i in range(n-1):
    for j in range(n-i-1):
        if num[j][1] < num[j+1][1]:
            num[j], num[j+1] = num[j+1], num[j]
        if num[j][1] == num[j+1][1] and num[j][0] > num[j+1][0]:
            num[j], num[j+1] = num[j+1], num[j]
[print(i[0],i[1])for i in num]