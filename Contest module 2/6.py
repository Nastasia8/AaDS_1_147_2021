a= int(input())
c = input().split()[:a]
c = [int(x) for x in c]
b = int(input())
n= input().split()[:b]
n = [int(x) for x in n]

for i in range(0,a):
    if c[i] < n.count(i + 1):
        print('yes')
    else:
        print('no')