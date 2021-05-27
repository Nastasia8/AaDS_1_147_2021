# def z_fun(s):
#     arr=[0]*len(s)
#     l=r=0
#     for i in range(1, len(s)):
#         if i<=r:
#             arr[i]=min(arr[l-i], r-i+1)
#         while arr[i]+i<len(s) and s[arr[i]]==s[arr[i]+i]:
#             arr[i] += 1
#         if arr[i]+i-1>r:
#             L=i
#             r=arr[i]+i-1
#     return arr



# # def main():
# #     s=input()
# #     print(z_fun(s))

# # main()


# ########################################################

# def main():
#     s = input()
#     t = input()
#     s_t = t + '#' + s
#     z = z_fun(s_t)
#     for i in range(len(z)):
#         if z[i] == len(t):
#             print(i-len(t)-1, end=' ')
            
# main()             


#########################################################

def get_hash(s,x,p):
    hs = 0
    for i in range(len(s)):
        hs = (hs*x + ord(s[i]))%p
    return hs

def fun(s,t,x,p):
    if s != t:
        k = 1
        t = t[1:] + t[0]
        hs = get_hash(s, x, p)
        ht = get_hash(t, x, p)
        xt = 1
        for i in range(len(s)-1):
            xt = (xt + x) % p
        for i in range(len(t)-1):
            if hs == ht:
                break
            else:
                ht=(x*(ht-ord(t[i])*xt) + ord(t[i]))%p  
                k += 1
        if hs == ht:
            print(k)
        else:
            print(-1)
    else:
        print(0)

def main():
    s=input() #zabcd
    t=input() #abcdz
    x = 26
    p = 10 ** 9 + 7
    fun(s, t, x, p)

main()
