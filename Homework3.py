#1

n = int(input())

def factorial(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n * factorial(n-1)

for i in range(1,n+1):

    answer = -1*i*((5-i)/factorial(i))
    
print(answer)

#2

def formula():

    for i in range(15):
        if i == 0:
            print(0)
        elif i == 1:
            print(3)
        else:
            print((i-1)+(i-2))

formula()

#3

text = ["Crime and Punishment", 1,331,1886, "The Master and Margarita", 1,470, 1996]

dictionary = {}

def sort_dict(text):
    for i in text:
        if type(i) == str:
            dictionary[i] = []
            temp = i
        else:
            dictionary[temp].append(i)
    return dictionary

print(sort_dict(text))

#4

text = ["Bass","Pike","Roach","Catfish","Trout","Mackerel","Salmon","Zander","Anchovy"]

text_sorted = ""

text_sorted = " ".join(text).lower().split()

answer = []

def sort_by_last_letter(text):
    for i in text:
        answer.append(i[-1])

    answer.sort()

    return answer

print(sort_by_last_letter(text_sorted))

#5

numbers = [14, 46, 10, -78, 0, 6, -31, -24, 56, 17, -83, -4]

dictionary = {}

for i in numbers:
    if i > 0:
        dictionary[i] = "Positive"
    elif i < 0:
        dictionary[i] = "Negative"
    else:
        dictionary[i] = "Zero"

print(dicti
      onary)







