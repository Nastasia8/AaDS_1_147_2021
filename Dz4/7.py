def func(lwords,sym):
    max_item = max(lwords,key = lambda x:len(x))
    max_len = len(max_item)
    return[item.ljust(max_len,sym) for item in lwords]
words = ["tiger",  "leopard", "elephant"]
print(func(words,"#"))