spis = ['Bass', 'Pike', 'Roach', 'Catfish', 'Trout', 'Mackerel', 'Salmon', 'Zander', 'Anchovy']
print(spis)

new_spis = sorted(spis, reverse=True)
print(new_spis)


for i in new_spis:
        print(i[-1:])
