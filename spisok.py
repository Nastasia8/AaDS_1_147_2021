result = 0
x = [7,1,3,4,3,9,14,-5,-17,-13,-19,-18]
i = 0

while i <= 11:
    if x[i]<0:
        result += x[i]
    i += 1
print(x, result)