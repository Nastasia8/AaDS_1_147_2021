def search (s):
    array=[0]*len(s) 
    l=r=0 
    for i in range(1,len(s)):
        if i<=r:
            array[i]=min(array[l-1],r-i+1)
        while array[i]+i<len(s) and s[array[i]]==s[array[i]+i]:
            array[i]+=1
        if array[i]+i-1>r:
            l=i
            r=array[i]+i-1
    return array
    
    
    
def main ():
    s = input()
    t = input()
    s_t = t+'#'+s
    z=search(s_t)
    for i in range(len(z)):
        if z[i]==len(t):
            print(i-len(t)-1,end = ' ')

main()