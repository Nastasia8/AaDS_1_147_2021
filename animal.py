animals = ['tiger', 'leopard', 'elephant', 'Fox', 'wolf', 'camel', 'raccoon']

def func(animals):
    animals[0], animals[-1] = animals[-1], animals[0]
    return(animals)
print(func(animals))
