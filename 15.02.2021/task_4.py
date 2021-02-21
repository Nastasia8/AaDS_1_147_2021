spis = '“Bass”, “Pike”, “Roach”, “Catfish”, “Trout”, “Mackerel”, '\
       '“Salmon”, “Zander”, “Anchovy”'.replace('“','').replace('”','').split(', ')
otdel = []
res = []
n = -1
m = -3

while n >= -len(spis):
    otdel = list(spis[n])
    while len(otdel) > 2:     
        del otdel[m]
    res += otdel
    m = -3
    n -= 1

res.sort(reverse = True)

print(spis)
print(res)
