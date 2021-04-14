#ТРЕНИРОВОЧНЫЕ ЗАДАЧИ:

#задача пробная 1
def preph(s):
    p=[0]*len(s)
    for i in range (len(s)-1):
        k=p[i] #значение
        while k>0 and s[i+1]!=s[k]:
            k=p[k-1]
        if s[i+1]==s[k]:
            p[i+1]=k+1
        else:
           p[i+1]=0
    return p

def main():
    s=input()
    print(preph(s))

main()

#задача пробная 2
def z_fun(s):
    arr=[0]*len(s)
    l=r=0
    for i in range(1,len(s)):
        if i<=r:
            arr[i]=min(arr[l-i],r-i+1)
            #arr[i]=(arr[l-i])
        while arr[i]+i<len(s) and s[arr[i]]==s[arr[i]+i]:
            arr[i]+=1
        if arr[i]+i-1>r:
            l=i
            r=arr[i]+i-1
    return arr

def main():
    s=input()
    print(z_fun(s))

main()

#задача пробная 3
def z_fun(s):
    arr=[0]*len(s)
    l=r=0
    for i in range(1,len(s)):
        if i<=r:
            arr[i]=min(arr[l-i],r-i+1)
            #arr[i]=(arr[l-i])
        while arr[i]+i<len(s) and s[arr[i]]==s[arr[i]+i]:
            arr[i]+=1
        if arr[i]+i-1>r:
            l=i
            r=arr[i]+i-1
    return arr

def main ():
    s=input()
    t=input()
    s_t=t+"#"+s
    z=z_fun(s_t)
    for i in range (len(z)):
        if z[i]==len(t):
            print(i-len(t)-1,end=" ")




#ОСНОВНЫЕ ЗАДАЧИ:

#задача1
def preph(s):
    p=[0]*len(s)
    for i in range (len(s)-1):
        k=p[i]
        while k>0 and s[i+1]!=s[k]:
            k=p[k-1]
        if s[i+1]==s[k]:
            p[i+1]=k+1
        else:
           p[i+1]=0
    return p

def main():
    s=input()
    t=input()
    s_t=t+"&"+s
    p=preph(s_t)
    for i in range(len(p)):
        if p[i]==len(t):
            print(i-2*len(t),end=" ")

main()


#задача2
def get_hash(s,x,p):
    hs=0
    for i in range (len(s)):
        hs=(hs*x+ord(s[i]))%p
    return hs

def fun(s,t,x,p):
    if s!=t:
        k=1
        t=t[1:]+t[0]
        hs=get_hash(s,x,p)
        ht=get_hash(t,x,p)
        xt=1
        for i in range(len(s)-1):
            xt=(xt*x)%p
        for i in range(len(t)-1):
            if hs==ht:
                break
            else:
                ht=(x*(ht-ord(t[i])*xt)+ord(t[i]))%p
                k+=1
        if hs==ht:
            print(k)
        else:
            print(-1)
    else:
        print (0)

def main():
    s=input() #zabcd
    t=input() #abcdz
    x=26
    p=1*10**9+7
    fun(s,t,x,p)

main()


#задача3
def preph(s):
    p=[0]*len(s)
    for i in range (len(s)-1):
        k=p[i]
        while k>0 and s[i+1]!=s[k]:
            k=p[k-1]
        if s[i+1]==s[k]:
            p[i+1]=k+1
        else:
           p[i+1]=0
    return p

def main():
    s=input()
    s_t=s+"&"+s
    p=preph(s_t)
    pr=p[-1]-p[len(s)-1]
    b=len(s)//pr
    if s[:pr]*b==s:
        print(b)
    else:
        print(1)
    
main()


#задача4
def prefix(s):
    p = [0]*len(s)
    for i in range(len(s)-1):
        j = p[i]
        while j>0 and s[j]!=s[i+1]:
            j=p[j-1]
        if s[j]==s[i+1]:
            p[i+1]= j+1
        else:
            p[i+1]=0
    return p

def main():
    s = input()
    s_t = s+"&"+s 
    a = prefix(s_t)
    p0=a[-1]-a[len(s)-1]
    print(p0)

main()