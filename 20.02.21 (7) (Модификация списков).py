def func1(lwords,sym):
     max_item=max(lwords,key=lambda x:len(x))
     max_len=len(max_item)
     return [item.ljust(max_len,sym)for item in lwords]

words1 = ["tiger", "leopard", "elephant", "camel", "fox", "wolf", "raccoon"]
words2 = ["Clematis", "Dahlia", "Rose", "Chrysanthemum", "Freesia", "Lily", "Peony"]
words3 = ["Bass", "Roach", "Catfish", "Trout", "Mackerel", "Anchovy"]
print(func1(words1, "#"))
print(func1(words2, "#"))
print(func1(words3, "#"))
