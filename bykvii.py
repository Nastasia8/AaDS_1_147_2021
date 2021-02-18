elements = '“Bass”, “Pike”, “Roach”, “Catfish”, “Trout”, “Mackerel”,“Salmon”, “Zander”, “Anchovy”'
otdel = []
result = []
n = -1
m = -3

while n >= -len(elements):
    otdel = list(elements[n])
    while len(otdel) > 2:     
        del otdel[m]
    result += otdel
    m = -3
    n -= 1

result.sort(reverse = True)
print(elements)
print(result)