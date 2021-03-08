def Function (Words,n):
    a=len(Words[0])
    for word in Words:
        if a<len(word):
            a=len(word)
    list_1=[]
    for word in Words:
        word = word.ljust(a,n)
        list_1.append(word)
    return list_1

list_1=["Clematis", "Dahlia", "Rose", "Chrysanthemum", "Freesia", "Lily", "Peony"]
list_2=["tiger","leopard","elephant","camel","fox","wolf","raccoon"]
list_3=["Bass","Roach","Catfish","Trout","Mackerel","Anchovy"]

n=input("Введите символ для дополнения слов: ")
list_1=Function(list_1,n)
print(list_1)

list_2=Function(list_2,n)
print(list_2)

list_3=Function(list_3,n)
print(list_3)