

def funk(words, symb):


    best = 0
    for index in range(len(words)):
        if len(words[index]) > len(words[best]):
            best = index
   
    max_len = len(words[best])
    return [item.ljust(max_len, symb) for item in words]
spisok = ["tiger", "leopard", "elephant"]

print(funk(spisok, "№"))