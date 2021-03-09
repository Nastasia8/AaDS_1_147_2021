a = '“Clematis”, “Dahlia”, “Rose”, “Chrysanthemum”, '\
    '“Freesia”, “Lily”, “Peony”'.replace('“','').replace('”','').split(', ')
b = '“tiger”, “leopard”, “elephant”, “camel”, '\
    '“fox”, “wolf”, “raccoon”'.replace('“','').replace('”','').split(', ')
c = '“Bass”, “Roach”, “Catfish”, “Trout”, “Mackerel”, '\
    '“Anchovy”'.replace('“','').replace('”','').split(', ')

def maxbucv(a):
    i = 0
    j = 0
    k = 0
    max = 0
    while i < len(a):
        while j < len(a[i]):
            k = k + 1
            j = j + 1
        if k > max:
            max = k
        i = i + 1
    if i == len(a):
        return(max)

def zapolnit(a, max):
    i = 0
    j = 1
    n = 0
    slovo = []
    while i < len(a):
        slovo = str(a[i])
        slovo = list(slovo)
        n = max - len(slovo)
        j = 0
        for j in range(j, n):
            a[i] = a[i] + '?'
            slovo.append(1)
        i = i + 1
    return(print(a))

max = maxbucv(a)
zapolnit(a, max)
max = maxbucv(b)
zapolnit(b, max)
max = maxbucv(c)
zapolnit(c, max)
