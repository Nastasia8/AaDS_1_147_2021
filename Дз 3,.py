#3.1
print ('Введите  N:')
n=float(input())
def summa(n):
    k=1
    sum=0
    while k<=n:
        sum +=(-1)*k*((5-k)/factorial(k))
        k+=1
    return (sum)
def factorial(k):
    if k>1:
        return k*factorial(k-1)
    return (k)
print (round(summa(n),2))
#3.2
def func(p):
    p[0]=0
    p[1]=3
    n=2
    while n<15:
        p[n]=p[n-1]+p[n-2]
        n+=1
    return(p)

print(func([0] * 15))
#3.3
def func():
    words=['Crime and Punishment', 1, 331, 1866, 'The Master and Margarita', 1, 470, 1966, 'War and Peace', 4, 1274, 1869, 'And Quiet Flows the Don', 4, 1600, 1940]
    dict={}
    stroka=''
    for word in words:
        if (type(word)==str):
            dict[word]=[]
            stroka=word
        else:
            dict[stroka].append(word)
    return (dict)
print (func())
#3.5
ist = [14, 46, 10, -78, 0, 6, -31, -24, 56, 17, -83, -4]
d = {}
for num in list:
   if num>0:
      d[num] = "positive"
   elif num<0:
      d[num] = "negative"
   else:
      d[num] = "zero"

print(d)

