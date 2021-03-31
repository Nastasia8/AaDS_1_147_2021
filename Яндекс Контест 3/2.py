s=input()
t=input()
n=len(s)
k=-1
for i in range (n+1):
    s1=list(s)
    s=''

    b=s1[-1]
    for j in range (n-1,0,-1):
        s1[j]=s1[j-1]
    s1[0]=b

    for j in range(len(s1)):
        s+=s1[j]
    if s==t:
        k=i+1
        break
print(k)