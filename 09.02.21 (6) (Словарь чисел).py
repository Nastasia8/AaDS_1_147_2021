dictionary = {'key1': 37, 'key2': 56, 'key3': -37, 'key4': 21}
result1 = 1
result2 = 0
for key in dictionary:    
    result1 = result1 * dictionary[key]
    result2 = result2 + dictionary[key]

print("Произведение= ",result1,"Сумма=",result2)
