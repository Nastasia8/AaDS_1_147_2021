def merge(one, two):
    spis = []
    i = 0
    j = 0
    inversion = 0
    while i < len(one) and j < len(two):
        if one[i] <= two[j]:
            spis.append(one[i])
            i += 1
        else:
            spis.append(two[j])
            j += 1
            inversion += len(one) - i
    while i < len(one):
        spis.append(one[i])
        i += 1
    while j < len(two):
        spis.append(two[j])
        j += 1
    return spis, inversion

def merge_sort(m):
    n = len(m)
    if n <= 1:
        return m, 0
    middle = n//2
    one, left = merge_sort(m[0:middle])    
    two, right = merge_sort(m[middle:n])
    spis, inversion = merge(one, two)
    return spis, inversion + left + right    

n = int(input())
m = list(map(int, input().split(" ")))
m, fin = merge_sort(m)
print(fin)