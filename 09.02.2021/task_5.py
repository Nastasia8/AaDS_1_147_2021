text = 'Hello hi how hello are and you I am fine '\
            'thank you and you hello You Thank And'.lower().split()
chislo = []
i = 0

while i < len(text):
    j = -1
    k = 0
    while j < len(text):
        if text[i] == text[j]:
            k += 1
        j += 1
    i += 1
    chislo.insert(i, k)
    
slov = dict(zip(text, chislo))
print(slov)
