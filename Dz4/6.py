sp = [1,2,4,5,6]
def func(sp):
    a = list()
    [a.append(num) for num in sorted(sp) if num not in a]
    return tuple(a)
numbers = [int(num) for num in input().split()]
print(func(numbers))