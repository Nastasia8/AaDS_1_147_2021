
#3.1

print ('Введите   количество повторений N:')
n=float(input())
def summa(n):
    k=1
    summ=0
    while k<=n:
        summ +=(-1)*k*((5-k)/factorial(k))
        k+=1
    return (summ)

def factorial(k):
    if k>1:
        return k*factorial(k-1)
    return (k)
print(round(summa(n),2)) 


#3.2

def func(n):
    if n==0:
        return 0
    if n==1:
        return 3
    return func(n-1) + func(n-2)


for i in range(0,16):
    print(func(i), end=" ")

#3.3

word=['Crime and Punishment', 1, 331, 1866, 'The Master and Margarita', 1, 470, 1966, 'War and Peace', 4, 1274, 1869, 'And Quiet Flows the Don', 4, 1600, 1940]
word = [word[i] for i in range(0, len(word), 4)]

dict={}

for i in word:
    if i in dict:
       dict[i]+=1
    else:
        dict[i]=1

print(dict)
   

#3.4
sp = ['Bass', 'Pike', 'Roach', 'Catfish', 'Trout', 'Mackerel', 'Salmon', 'Zander', 'Anchovy']
print(sorted([word[-1] for word in sp], reverse=True)) 

#3.5
list = [14, 46, 10, -78, 0, 6, -31, -24, 56, 17, -83, -4]
d = {}

for num in list:
   if num>0:
      d[num] = "positive"
   elif num<0:
      d[num] = "negative"
   else:
      d[num] = "zero"

print(d)