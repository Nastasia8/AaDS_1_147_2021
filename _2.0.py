#2.1
#2.1.1
def func(list_sp):
    new_list=[]
    for number in list_sp:
        if number%2==0:
            new_list.append(number)
    print (new_list)

a=[3, 8, 2, 1, 4, 7, 5, 6, 10, 9]
func(a)

#2.1.2

a=[3, 8, 2, 1, 4, 7, 5, 6, 10, 9]
print ([num for num in a if num %2==0])

#2.1.3

def fun(number):
    return number %2==0
a=[3, 8, 2, 1, 4, 7, 5, 6, 10, 9]
print (list(filter(fun,a)))

#2.1.4

def fun(number):
    return number %2==0
sp=list(range(1,11))
print (list(filter(lambda number:number%2==0,sp)))



#2.2

list = [ 'tiger', 'leopard', 'elephant', 'fox', 'wolf', 'camel', 'raccoon']
list[0], list[-1] = list[-1], list[0]
print(list) 


#2.3

def change(input_set, input_list):
    for i in input_set:
        if i not in input_set:
            return False
        return True

print(change({1, 2, 'a', 4}, [5]))

#2.4

a=(1, 2, 2, 3, 1, 2, 4, 3, 2, 2)
b=[]
for i in range (len(a)):
    if a[i]==2:
        b.append(i)
print (b)

#2.5

text="Hello hi how hello are and you I am fine thank you and you hello You Thank And".lower().split()
d={}
for a in text:
    if a in d:
        d[a]+=1
    else:
        d[a]=1
print(d)

for word in text:
    d[word]=d.get(word,0)+1
print(d)

#2.6
dict= {'1': 5, '2': 2, '3': 3, '4': 7}
umno= 1
summa = 0
for i in dict:
    umno*=dict[i]
    summa+=dict[i]

print("Произведение= ",umno,"Сумма=",summa)

#2.7
print(":D")

#2.8
print(":(")
