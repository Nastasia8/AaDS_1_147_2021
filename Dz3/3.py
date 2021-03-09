words = ["Crime and Punishment", 1, 331, 1866, "The Master and Margarita", 1, 470, 1966, "War and Peace", 4, 1274, 1869, "And Quiet Flows the Don", 4, 1600, 1940]
d={}
s = ""
for a in words:
    if type(a) == str:
        d[a] = []
        s =a
    else:
        d[s].append(a)
print(d)