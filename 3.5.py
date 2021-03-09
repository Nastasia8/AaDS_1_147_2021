list = [14, 46, 10, -78, 0, 6, -31, -24, 56, 17, -83, -4]
Dict={}
for i in list:
    if i > 0:
        Dict[i]="positive"
    elif i < 0:
        Dict[i]="negative"
    else:
        Dict[i]="zero"
print(Dict)