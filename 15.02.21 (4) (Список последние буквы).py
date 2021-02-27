string="Bass, Pike, Roach, Catfish, Trout, Mackerel, Salmon, Zander, Anchovy"
letters = []
for word in string.split(", "):
    letters.append(word[-1])
print (sorted(letters, reverse=True))
