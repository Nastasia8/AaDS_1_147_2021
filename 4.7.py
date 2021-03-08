def func(Words, n):
    a = len(Words[0])
    for word in Words:
        if a < len(word): 
            a = len(word)
    list_one = []
    for word in Words:
        word = word.ljust(a, n)
        list_one.append(word)
    return list_one 

list_one = ['Clematis', 'Dahlia', 'Rose', 'Chrysanthemum','Freesia', 'Lily', 'Peony']
list_two = ['tiger', 'leopard', 'elephant', 'camel', 'fox', 'wolf', 'raccoon']
list_three = ['Bass', 'Roach', 'Catfish', 'Trout', 'Mackerel', 'Anchovy'] 

n = input('Введите элемент для 1 списка:')
list_one = func(list_one, n)               
print(list_one)

m = input('Введите элемент для 2 списка:')
list_two = func(list_two, m)               
print(list_two)

b = input('Введите элемент для 3 списка:')
list_three = func(list_three, b)               
print(list_three)