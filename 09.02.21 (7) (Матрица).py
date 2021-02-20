a = [[1,2,3],
     [4,5,6],
     [7,8,9]]

def m(a):
    print(a)
    for i in range(len(a)):
        a[i][len(a)-i-1] *= 2
    print(a)

print(m(a))

