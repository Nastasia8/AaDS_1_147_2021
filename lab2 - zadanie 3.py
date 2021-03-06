a=["Clematis", "Dahlia", "Rose", "Iris", "Chrysanthemum", "Freesia", "Astilba", "Lily", "Peony"]
b=[]
for i in a:
    b.append(i[-1])
print([i[-1] for i in a])    
print(list(map(lambda x: x[-1],a))) 