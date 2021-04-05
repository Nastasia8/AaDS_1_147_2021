def funct(s):
    k = 0
    l = []
    for i in s:
        if (i == '('):
            l.append(i)
        elif (l != []) and (l[-1] == '('):
            l.pop()
        else:
            k += 1
    return k+len(l)
    
s = input()
print(funct(s))