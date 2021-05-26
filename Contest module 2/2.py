a=int(input())

m=[]
for i in range(a):
    k, v=map(int, input().split())
    m.append([k,v])
m.sort(key=lambda x: x[0])
m.sort(key=lambda x: x[1], reverse = True)
[print(i[0], i[1]) for i in m]