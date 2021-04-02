def prefix(s):
    v = [0]*len(s)
    for i in range(len(s)-1):
        k = v[i]
        while k > 0 and s[k] != s[i+1]:
            k = v[k-1]
        if s[i+1] == s[k]:
            v[i+1] = k+1
        else:
            v[i+1] = 0
        
    return v

def main():
    s=input()
    s_t = s +"$" + s
    a = prefix(s_t)
    end = a[-1] - a[len(s)-1]
    print(end) 

main()    
