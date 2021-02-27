animals = ['tiger', 'leopard', 'elephant', 'Fox', 'wolf', 'camel', 'raccoon']

def func(animals):
    animals[0], animals[6] = animals[6], animals[0]
    return(animals)
print(func(animals))