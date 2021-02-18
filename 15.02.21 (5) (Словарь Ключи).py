list = [14, 46, 10, -78, 0, 6, -31, -24, 56, 17, -83, -4]
d = {}
for num in list:
   if num>0:
      d[num] = "positive"
   elif num<0:
      d[num] = "negative"
   else:
      d[num] = "zero"

print(d)
