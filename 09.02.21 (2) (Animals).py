animals=['tiger', 'leopard', 'elephant', 'fox', 'wolf', 'camel', 'raccoon']
h = animals.index("raccoon")
removed_item = animals.pop(h)  
animals.append ('tiger')
animals.insert (0,'raccoon')
i = animals.index('tiger')
removed_item = animals.pop(i)  
print (animals)
animals.clear()
