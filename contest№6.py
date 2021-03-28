sklad=int(input())
products=list(map(int,input().split()))
zakaz=int(input())
order=list(map(int,input().split()))
count=[0]*(sklad+1)
for now in order:
    count[now]+=1
for i in range(sklad):
    if products[i]<count[i+1]:
        print ('yes')
    else:
        print ('no')