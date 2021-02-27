#задача 1, способ 1
def fun(list_a):
    new_list=[]
    for number in list_a:
        if number %2==0:
            new_list.append(number)
    print(new_list)

a=[3, 8, 2, 1, 4, 7, 5, 6, 10, 9]
fun(a)

#способ 2
a=[3, 8, 2, 1, 4, 7, 5, 6, 10, 9]
print([num for num in a if num%2==0])


#способ 3
def fun(number):
    return number%2==0

a=[3, 8, 2, 1, 4, 7, 5, 6, 10, 9]

print(list(filter(fun,a)))


#cпособ 4
def fun(number):
    return number%2==0

a=[3, 8, 2, 1, 4, 7, 5, 6, 10, 9]

print(list(filter(lambda number:number%2==0,a)))


#задача 2,способ 1
a=["tiger", "leopard", "elephant", "Fox","wolf", "camel", "raccoon"]
new_a=a.pop(0)
new_a=a.insert(6, "tiger")
new_b=a.pop(5)
new_b=a.insert(0, "racoon")

print(a)

#способ 2
a=["tiger", "leopard", "elephant", "Fox","wolf", "camel", "raccoon"]

def change (words):
    words[0],words[-1]=words[-1],words[0]
    return words
print(change(a))


#задача 3
def change(input_set,input_list):
    for i in input_list:
        if i not in input_set:
            return False
        return True
print(change({1,2,"a",4},[5]))


#задача 4
a=(1, 2, 2, 3, 1, 2, 4, 3, 2, 2)
a=list(a)
n=0
for i in a:
    if i==2:
        print(n)
    n+=1
#не понимаю как сделать, чтоб списком выводилось     




#задача 5, способ 1
Text="Hello hi how hello are and you I am fine thank you and you hello You Thank And".lower().split( ' ')
dict={}
for word in Text :
    if word in dict:
        dict[word]+=1
    else:
        dict[word]=1

print(dict)

#способ 2
Text="Hello hi how hello are and you I am fine thank you and you hello You Thank And".lower().split( ' ')
dict={}
for word in Text :
    dict[word]=dict.get(word,0)+1

print(dict)

#способ 3
Text="Hello hi how hello are and you I am fine thank you and you hello You Thank And".lower().split( ' ')
dict={}
for word in Text :
    dict[word]=dict.get(word,0)+1

print({n: Text.count(n) for n in Text})



#задача6
slovar = {'number1': 81, 'number2': -12, 'number3': 33, 'number4': 100}
proizvedenie = 1
summa = 0
for number in slovar:    
    proizvedenie*= slovar[number]
    summa+= slovar[number]

print("Произведение элементов словаря= ",proizvedenie,"Сумма элементов словаря=",summa)


#задача7
#не справилась

#задача8
kort=(1, 2, 3, 4, 5, 4, 6, 2, 4, 7, 9, 4, 5, 6, 5, 0, 4, 2)
element=input("Введите значение элемента: ")

def func(kort,element):
    if element in kort:
        if kort.count(element)>1:
            first_ind=kort.index(element)
            last_int=kort.index()   #не понимаю как обозначить индекс последнего такого элемента
            return kort[first_ind:last_int]
        else:
            return kort[first_ind:]
    else:
        print("Символа нет в кортеже")















