def division(mass, start, end):
    if end - start > 1:
        half = (start + end) // 2
        division(mass, start, half)
        division(mass, half, end)
        left = mass[start:half]
        right = mass[half:end]
        func(mass, left, right, start)
        print(start + 1, end, mass[start], mass[end - 1]) 
        
def func(mass, left, right, start):
    i = j = 0
    while i < len(right) and j < len(left):
        if left[j] > right[i]:
            mass[start] = right[i]
            i= i + 1
        else:
            mass[start] = left[j]
            j = j + 1
        start = start + 1
    while i < len(right):   
        mass[start] = right[i]
        i = i + 1
        start = start + 1
    while j < len(left):
        mass[start] = left[j]
        j = j + 1
        start = start + 1 
        
N = int(input())
mass = list(map(int, input().split()))
division(mass, 0, N)
print(*mass, sep = ' ')
