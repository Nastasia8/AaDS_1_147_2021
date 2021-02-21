a = list(range(1, 26))
b=[]
for num in a:
   if num%2==0:
      b.append(num**2)
for num in b:
   print(num)

print([i**2 for i in a if i%2==0])