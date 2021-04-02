def z_fun (s):
    arr=[0]*len(s)
    l=r=0 
    for i in range(1,len(s)):
        if i<=r:
            arr[i]=min(arr[i-l],r-i+1)
        while arr[i]+i<len(s) and s[arr[i]]==s[arr[i]+i]:
            arr[i]+=1
        if arr[i]+i-1>r:
            l=i
            r=arr[i]+i-1
    return arr
    
    
    
def main ():
    s=input()
    t=input()
    s_t=t+'#'+s
    z=z_fun(s_t)
    for i in range(len(z)):
        if z[i]==len(t):
            print (i-len(t)-1,end=' ')
main()
