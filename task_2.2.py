animals = ['tiger', 'leopard', 'elephant', 'Fox', 'wolf', 'camel', 'raccoon']

def func(animals):
    j = animals[0]
    animals[0] = animals[6]
    animals[6] = j
    return(animals)

print(func(animals))
