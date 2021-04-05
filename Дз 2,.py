#2.1
#1 способ
def fan(list_a):
    new_list=[]
    for number in list_a:
        if number%2==0:
            new_list.append(number)
    print (new_list)
    
a=[3, 8, 2, 1, 4, 7, 5, 6, 10, 9]
fan(a)
#2 способ
a=[3, 8, 2, 1, 4, 7, 5, 6, 10, 9]
print ([num for num in a if num %2==0])
#3 способ
def fun(number):
    return number %2==0
a=[3, 8, 2, 1, 4, 7, 5, 6, 10, 9]
print (list(filter(fun,a)))
#4 способ
def fun(number):
    return number %2==0
a=list(range(1,11))
print (list(filter(lambda number:number%2==0,a)))
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
#2.5
text = 'Hello hi how hello are and you I am fine thank you and you hello You Thank And'.lower().split(' ')
dict = {}
for word in text:
#     if word in dict:
#         dict[word]+=1
#     else:
#         dict[word]=1
    dict[word]=dict.get(word,0)+1
print(dict)    
#2.6
dictionary = {'key1': 37, 'key2': 56, 'key3': -37, 'key4': 21}
result1 = 1
result2 = 0
for key in dictionary:    
    result1 = result1 * dictionary[key]
    result2 = result2 + dictionary[key]

print("Произведение= ",result1,"Сумма=",result2)
#2.7
a = [[1,2,3],
     [4,5,6],
     [7,8,9]]

def print_massive(arr):
    for i in range(len(arr)):
      for j in range(len(arr[i])):
        print(arr[i][j] , end= "\t")
      print()

print_massive(a)
#2.8
num=(1, 2, 3, 4, 5, 4, 6, 2, 4, 7, 9, 4, 5, 6, 5, 0, 4, 2)
print ('Введите значение элемента: ')
x=float(input())
def fun(num,x):
    if x in num:
        start=num.index(x)
        k=num.count(x)
        if k>1:
            i=1
            end=start
            while i<k:
                end=num.index(x,end+1)
                i+=1
            print (num[start:end+1])
        else:
            print (num[start:])
    else:
        print('x не входит')
fun(num,x)