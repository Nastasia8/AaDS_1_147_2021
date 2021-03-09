a=[14, 46, 10, -78, 0, 6, -31, -24, 56, 17, -83, -4]
dict = {}
for i in a:
    if i > 0:
       dict[i]="positive"
    elif i < 0:
       dict[i]="negative"
    else i == 0:
        dict[i]="zero"
print(dict) 