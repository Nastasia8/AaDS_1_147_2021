# def preph (s):
#     p=[0]*len(s)
#     for i in range (len(s)-1):
#         k=p[i]
#         while k>0 and s[i+1]!=s[k]:
#             k=p[k-1]
#         if s[i+1]==s[k]:
#             p[i+1]=k+1
#         else: 
#             p[i+1]=0
#     return p

# s=input()
# print (preph(s))

def prefix(s):
    v = [0]*len(s)
    for i in range(1,len(s)):
        k = v[i-1]
        while k > 0 and s[k] != s[i]:
            k = v[k-1]
        if s[k] == s[i]:
            k = k + 1
        v[i] = k
    return k

s=input()
print(prefix(s))    
