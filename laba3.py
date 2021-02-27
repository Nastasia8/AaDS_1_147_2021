#задача1
print ("Введите n: ", end=" ")
n=int(input())

def func (n):
    k=1
    s=0
    while k<=n:
        s+=(-1)*k*((5-k)/factorial(k))
        k+=1
    return (s)

def factorial(k):
    if k>1:
        return k*factorial(k-1)
    return(k)

print ("Сумма числового ряда = " , round(func(n),3))

#задача2
def func(n):
    if n==0:
        return 0
    if n==1:
        return 3
    return func(n-1) + func(n-2)


for i in range(0,16):
    print(func(i), end=" ")

#задача3
slovar=["Crime and Punishment", 1, 331, 1866, "The Master and Margarita", 1, 470, 1966, "War and Peace", 4, 1274, 1869, "And Quiet Flows the Don", 4, 1600, 1940]
slovar = [slovar[i] for i in range(0, len(slovar), 4)]

dict={}

for word in slovar:
    if word in dict:
       dict[word]+=1
    else:
        dict[word]=1

print(dict)


#задача4, не поняла как буквы отсортировывать
string="Bass, Pike, Roach, Catfish, Trout, Mackerel, Salmon, Zander, Anchovy,"

#задача5
a = [14, 46, 10, -78, 0, 6, -31, -24, 56, 17, -83, -4]
print({x: "positive" if x > 0 else "negative" if x < 0 else "zero" for x in a})
