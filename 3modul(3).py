#Дана непустая строка S.
# Нужно найти такое наибольшее число k и строку T, что S совпадает со строкой T, выписанной k раз подряд.
 
def pref(S):
    p=[0]*len(S)
    for i in range(len(S)-1):
        j=p[i]
        while (j>0) and (S[i+1] !=S[j]):
            j=p[j-1]
        if (S[i+1]==S[j]):
            p[i+1]=j+1
        else:
            p[i+1]=0
    return p
S=input()
p=pref(S)
res=len(S)-p[-1]
if (len(S)%res==0):
    print(len(S)//res)
else:
    print('1')