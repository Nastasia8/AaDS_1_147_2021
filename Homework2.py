#1.1

a = [3, 8, 2, 1, 4, 7, 5, 6, 10, 9]
b = []

for i in range(len(a)):
    if a[i] % 2 == 0:
        b.append(a[i])

print(b)

#1.2

print([i for i in a if i%2 == 0])

#1.3

def filter_odd(a):
    return a%2 == 0

print(list(filter(filter_odd, a)))

#1.4

print(list(filter(lambda i: i%2==0, a)))

#1.5

def parity(a):
    i = 0 
    while i < len(a):
        if a[i]%2 == 0:
            print("even")
        else:
            print("odd")
        i += 1
        
print(parity(a))

#1.6

b.sort()
print(b)

#2

animals = ["tiger", "leopard", " elephant", "Fox", "wolf", "camel", "raccoon"]

def change(a):
    a[0], a[-1] = a[-1], a[0]
    return a

print(change(animals))

#3

a = set()
b = []

def check(a = set(),b = []):
    if a == b:
        return True
    else:
        return False
    
print(check(a,b))

#4

a = (1, 2, 2, 3, 1, 2, 4, 3, 2, 2)
b = []

def check(a):
    for i in range(len(a)):
        if a[i] == 2:
            b.append(i)
    return b
    
print(check(a))

#5

text = "Hello hi how hello are and you I am fine thank you and you hello You Thank And".lower().split(' ')

dict = {}

for word in text:
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1

print(dict.get("hello"))

print({"hello":dict.get(text) for text in dict})

#6

dict = {'key1': 1,
        'key2': 2}

print(sum(dict.values()))

def multiply(d):
    res = 1
    for i in d:
        res *= i

print(filter(multiply, list(dict.values())))

#7

a = [[1,2,3],
     [1,2,3],
     [1,2,3]]

def m(a):
    print(a)
    for i in range(len(a)):
        a[i][len(a)-i-1] *= 2
    print(a)

print(m(a))

#8

a = (1, 2, 3, 4, 5, 4, 6, 2, 4, 7, 9, 4, 5, 6, 5, 0, 4, 2)

n = int(input())

def res(a,n):
    if n in a:
        s = 0
        e = 0 
        while a[s] != n:
            s += 1
        while a[e] != n:
            e -= 1
        return(a[s:e])
    else:
        return(f"This tuple dosen't contains: {n}")
        
print(res(a,n))
        
        



