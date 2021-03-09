
Text= ["Crime and Punishment", 1, 331, 1866, "The Master and Margarita", 1, 470, 1966, "War and Peace", 4, 1274, 1869, "And Quiet Flows the Don", 4, 1600, 1940]
dict={}
s = ""
for a in Text:
    if type(a) == str:
        dict[a] = []
        s =a
    else:
        dict[s].append(a)
print(dict)