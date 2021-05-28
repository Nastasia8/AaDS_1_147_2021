#1

x = int(input())
y = int(input())

def GCD(x,y):

    n = 1
    
    while n <= x and n <= y:
        if x % n == 0 and y % n == 0:
            temp = n
            
        n += 1

    return temp

print(GCD(x,y)) # strange way to do this

def GCD_normal(x,y):

    while x != 0 and y != 0:
        
        if x > y:
            x = x % y
        else:
            y = y % x

    if x != 0:
        return x
    else:
        return y

print(GCD_normal(x,y))

#2

x = int(input())
y = int(input())

def LCM(x,y):

    n = x * y
    
    while x != 0 and y != 0:
        if x > y:
            x %= y
        else:
            y %= x
    return n // (x + y)

print(LCM(x,y))

#3

n = int(input())

def lead_to_one(n):

    numbers = []
    
    while n != 1:
        if n % 2 == 0:
            n = n//2
            numbers.append(n)
        else:
            n = (n*3) + 1
            numbers.append(n)

    return [n, numbers]

print(lead_to_one(n))

#4

matrix = [[4,3,5,1],
          [0,7,2,9],
          [2,6,3,8]]

def change(matrix):

    right = 1
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])//2):
            matrix[i][j],matrix[i][j-right] = matrix[i][j-right],matrix[i][j]
            
            right += 2

        right = 1
    
    return matrix

print(change(matrix))

#5

numbers = [1, 7, 4, 7, 15, 4, 7, 5, 2]

check = 1

def create_set(numbers):

    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if numbers[i] == numbers[j]:
                temp = str(numbers[j])
                check += 1
                temp *= check
                numbers[j] = temp

        check = 1

    return set(numbers)

print(create_set(numbers))

#6

border = int(input())

numbers = [int(i) for i in input().split()][:border]

def sort_bubble(numbers):

    for i in range(border - 1):
        for j in range(border - i - 1):
            if numbers[j] > numbers[j+1]:
                numbers[j],numbers[j+1] = numbers[j+1],numbers[j]

    return tuple(numbers)

print(sort_bubble(numbers))

#7

a = ["Clematis","Dalhia"]

b = ["tiger","leopard"]

c = ["Bass","Roach"]

def add_distance(words, symbol):

    temp = symbol

    max_distance = 1

    for i in words:
        if len(i) > max_distance:
            max_distance = len(i)

    for i in range (len(words)):
        if len(words[i]) < max_distance:
            dif = max_distance - len(words[i])
            symbol *= dif
            words[i] += symbol

        symbol = temp

    return words

print(add_distance(a, '#'))
        
            

    
            
            
            
        
            


    

