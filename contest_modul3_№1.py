def preph(s):
    x=[0]*len(s)
    for i in range(len(s)-1):
        v=x[i]
        while v>0 and s[i+1]!=s[v]:
            v=x[v-1]
        if s[i+1]==s[v]:
            x[i+1]=v+1
        else:
            x[i+1]=0
    return x
def main():
    s=input()
    t=input()
    itog=t+'&'+s
    x=preph(itog)
    for i in range(len(x)):
        if x[i]==len(t):
            print(i-2*len(t),end=' ')
          
main()